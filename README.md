<p align="center"><img src="docs/logo.svg" width="96" alt="" /></p>

# binlayer

[![CI](https://github.com/Gulliby-development/binlayer/actions/workflows/ci.yml/badge.svg)](https://github.com/Gulliby-development/binlayer/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

binlayer is a FIFO stock ledger built from SQLite tables, triggers, and views. It is for small shops and workshops that record receipts, sales, and discarded stock, and for bookkeepers or database users who want to inspect inventory and costing reports. The Python command-line program creates a fresh in-memory database for each run, loads the SQL files in sorted filename order, executes the SQL script supplied on standard input, and prints one selected view.

All quantities are positive integers in movement records; movement kind determines whether stock is added or removed. Money is stored and calculated as whole integer cents, and views do not return floating-point money. Movements are processed per SKU by day and then by movement ID, so inserting a movement with an earlier day still places it earlier in the ledger's processing order.

## Requirements and setup

Python 3.10 or newer is required. The program uses the SQLite library bundled with Python and supports Windows, macOS, and Linux.

From the repository directory, create an environment and install the development dependencies:

```sh
python -m venv .venv
```

Activate it in the shell you use:

- POSIX shells (macOS/Linux): `. .venv/bin/activate`
- PowerShell: `.venv\\Scripts\\Activate.ps1`
- Windows Command Prompt: `.venv\\Scripts\\activate.bat`

Then install the pinned development requirements:

```sh
pip install -r requirements-dev.txt
```

## Command-line use

Run `python binlayer.py VIEW` and send a SQL setup script on standard input. The script is UTF-8 text and can contain any number of statements. For example, use a pipe or redirect a file:

```sh
python binlayer.py balance < movements.sql
```

The program loads every `sql/*.sql` file in sorted filename order before running your script. It prints no headers: each result row is one line, with columns separated by `|`. A SQL NULL value is printed as `NULL`; an empty result prints nothing. Rows are ordered by the command's view registry. This listing order is separate from the day/ID processing order used to calculate ledger values; each view's listing keys are stated below.

A successful query exits with status 0. A SQLite error in the input script or query is written to standard error with the `binlayer:` prefix and exits with status 1. An absent or unrecognized view argument prints the usage message to standard error and exits with status 2.

## Data model and validation

The schema has three tables:

- `item(sku, name, reorder_level)` stores an item's name and its threshold for replenishment. The reorder level must be an integer of at least zero.
- `movement(id, sku, day, kind, qty, unit_cents)` is the append-only ledger. A receipt adds stock and records its per-unit cost; an issue is a sale and a scrap is stock thrown away. Quantity must be positive. Only receipts carry `unit_cents`, which is an integer number of cents and may be zero.
- `setting(name, val)` stores reporting parameters. Supported settings are `as_of`, a valid date, and `cover_window`, a number of days.

Movement checks run in this priority order, and the first failing check supplies the error:

1. Kind must be `receipt`, `issue`, or `scrap`: `bad kind`.
2. SKU must be text containing 1–12 lowercase letters, digits, or hyphens: `bad sku`.
3. Day must be a real calendar date in `YYYY-MM-DD` form from `1970-01-01` through `2999-12-31`: `bad day`.
4. Quantity must be an integer from 1 through 1,000,000: `bad quantity`.
5. A receipt must supply a unit cost: `receipt needs unit_cents`.
6. A receipt's unit cost must be an integer from 0 through 100,000,000 cents: `bad unit_cents`.
7. An issue or scrap must not supply a unit cost: `only receipts have unit_cents`.

The movement checks above validate INSERT values after SQLite has applied the table's normal affinity rules. The item and setting value guards also apply on INSERT: an invalid item threshold raises `bad reorder_level`; a setting name other than `as_of` or `cover_window` raises `unknown setting`; an invalid date raises `bad as_of`; and an invalid window raises `bad cover_window`. A cover window is its canonical decimal integer text from 1 through 365: signs, blanks, leading zeroes, and decimal notation are not accepted. These value guards do not describe UPDATE validation. Separately, triggers reject UPDATE or DELETE statements affecting an existing movement with `movements are append-only`; an update or delete that matches no row raises no error.

The FIFO cost and valuation views assume a non-oversold ledger: no SKU has issues or scraps exceeding available receipts in processing order. Diagnostics can still report negative balances, but FIFO allocations are not defined for an oversold ledger. The `as_of` setting selects report windows or ages stock; it does not reconstruct historical remaining inventory. Remaining-layer views always reflect all movements in the current ledger.

## Views

The CLI supports nineteen views. Columns are printed in the order shown; dates use `YYYY-MM-DD`, and monetary values are integer cents.

### Balances and diagnostics

- `balance(sku, on_hand)` — one row per SKU with movements; receipts less issues and scraps. Listed by SKU.
- `running(id, sku, day, kind, qty, on_hand)` — the balance immediately after each movement, in per-SKU day/ID processing order. Zero and negative balances are retained. Listed by SKU, day, then movement ID.
- `problems(id, sku, day, problem)` — one `short` row for every movement that leaves a negative balance. A SKU with no matching item also gets one `no item` row, at its lowest movement ID. If both apply to that ID, `no item` sorts first. Listed by movement ID, then problem text.

### FIFO and costing

Receipt layers and takes occupy consecutive positions on a separate unit line for each SKU, processing movements by day and ID. Issues and scraps share take positions. Each interval is half-open: the first position is included and the last is excluded.

- `layer(receipt_id, sku, day, qty, unit_cents, first_pos, last_pos)` — each receipt's interval and per-unit cost. Listed by SKU, then first position.
- `take(issue_id, sku, day, kind, qty, from_pos, to_pos)` — each issue or scrap's interval on the take line. Listed by movement ID (`issue_id`), not by processing day.
- `draw(issue_id, receipt_id, qty, unit_cents, cost_cents)` — positive overlaps between take and receipt intervals; cost is overlap quantity times the layer's unit cost. Listed by issue ID, then receipt ID.
- `issue_cost(issue_id, sku, day, kind, qty, drawn, cost_cents)` — each take and the total quantity and cost drawn for it. Listed by issue ID.
- `monthly(month, sku, issued, scrapped, cogs_cents, scrap_cents)` — monthly issue and scrap quantities and their separate costs, for SKU/month pairs with a take. Listed by month, then SKU.
- `month_total(month, cogs_cents, running_cents)` — monthly cost of issues across SKUs and its cumulative total across months present in the ledger. Listed by month.

### Remaining stock and valuation

- `layer_left(receipt_id, sku, left_qty, unit_cents, value_cents)` — unused quantity and value by receipt layer; fully consumed layers are omitted. Listed by receipt ID.
- `stock_value(sku, on_hand, value_cents)` — remaining quantity and total value by SKU, including stock whose cost is zero. Listed by SKU.
- `avg_cost(sku, on_hand, avg_cents)` — value per remaining unit, rounded half up to whole cents using integer arithmetic. Listed by SKU.

### Calendar and zero-stock history

- `calendar(day)` — every calendar date between the earliest and latest movement dates, inclusive; empty if there are no movements. Listed by day.
- `daily(sku, day, on_hand)` — each SKU's end-of-day balance from its first movement date through the global last movement date. Listed by SKU, then day.
- `empty_spans(sku, start_day, end_day, days)` — maximal consecutive runs of daily rows whose balance is exactly zero, including runs that continue through the final calendar day. Listed by SKU, then start day.

### Availability and stock reports

- `reorder(sku, name, on_hand, reorder_level, short)` — items below their threshold; items with no movements have zero on hand. `short` is the threshold minus stock on hand. Listed by SKU.
- `cover(sku, on_hand, used, cover_days)` — positive current balances and issue-only usage over the configured window. Requires `as_of`; the lower date is exclusive and `as_of` is inclusive. `cover_window` defaults to 30 days. Coverage is integer division of on-hand times window days by usage, or NULL when usage is zero. Scraps are excluded; with no `as_of`, this view has no rows. Listed by SKU.
- `aging(sku, bucket, qty, value_cents)` — remaining stock received no later than `as_of`, grouped into inclusive age ranges `0-30`, `31-60`, and `61+` days. Requires `as_of`; future receipts are excluded. Listed by SKU, then bucket.
- `abc(pos, sku, value_cents, class)` — ranks stock value descending, breaking ties by SKU ascending. A row is A when the value before it is below 80% of total value, otherwise B when below 95%, otherwise C. If total value is zero, all rows are C. Listed by position.

## Examples

The following transcripts are for a POSIX shell in the repository directory:

```text
$ printf "insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-09','issue',4,null);" | python binlayer.py issue_cost
2|a|2026-01-09|issue|4|4|800
$ printf "insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-09','issue',4,null);" | python binlayer.py stock_value
a|6|1200
$ printf "insert into movement values(null,'a','2026-02-30','receipt',1,1);" | python binlayer.py balance 2>&1; echo "exit $?"
binlayer: bad day
exit 1
$ python binlayer.py nope 2>&1; echo "exit $?"
usage: binlayer.py VIEW < script.sql
exit 2
```

## Development

Install the development requirements, then run these checks from the repository directory:

```sh
python -m sqlfluff lint sql
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

See [LICENSE](LICENSE) for the MIT license.

---

Built with [BAKED](https://github.com/Gulliby-development/baked), an open-source coding agent (bench round R86).
