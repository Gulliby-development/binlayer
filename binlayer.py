"""binlayer: a FIFO stock ledger kept in SQLite views.

Usage: python binlayer.py VIEW < script.sql
"""

import sqlite3
import sys
from pathlib import Path

SQL_DIR = Path(__file__).resolve().parent / "sql"

USAGE = "usage: binlayer.py VIEW < script.sql\n"

# The views the command line prints, each with the ORDER BY of its listing.
VIEWS = {
    "balance": "sku",
    "running": "sku, day, id",
    "problems": "id, problem",
    "layer": "sku, first_pos",
    "take": "issue_id",
    "draw": "issue_id, receipt_id",
    "issue_cost": "issue_id",
    "layer_left": "receipt_id",
    "stock_value": "sku",
    "avg_cost": "sku",
    "monthly": "month, sku",
    "month_total": "month",
    "calendar": "day",
    "daily": "sku, day",
    "empty_spans": "sku, start_day",
    "aging": "sku, bucket",
    "reorder": "sku",
    "cover": "sku",
    "abc": "pos",
}


def connect():
    """A new in-memory database with every file of sql/ applied in name order."""
    conn = sqlite3.connect(":memory:")
    for path in sorted(SQL_DIR.glob("*.sql")):
        conn.executescript(path.read_text(encoding="utf-8"))
    return conn


def render(rows):
    """One line per row, cells joined by `|`, NULL written as NULL."""
    lines = ("|".join("NULL" if cell is None else str(cell) for cell in row) for row in rows)
    return "".join(line + "\n" for line in lines)


def main(args):
    if len(args) != 1 or args[0] not in VIEWS:
        sys.stderr.write(USAGE)
        return 2
    script = sys.stdin.buffer.read().decode("utf-8")
    conn = connect()
    try:
        conn.executescript(script)
        rows = conn.execute(f"select * from {args[0]} order by {VIEWS[args[0]]}").fetchall()
    except sqlite3.Error as error:
        sys.stderr.buffer.write(f"binlayer: {error}\n".encode("utf-8"))
        return 1
    finally:
        conn.close()
    sys.stdout.buffer.write(render(rows).encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
