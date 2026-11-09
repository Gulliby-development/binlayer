from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a1234567890b','2026-01-05','receipt',5,200);", "balance", "a1234567890b|5\n"),
    row("insert into movement values(null,'a','2026-01-05','return',5,200);", "balance", "error: bad kind\n"),
    row("insert into movement values(null,'A','2026-02-30','gift',0,null);", "balance", "error: bad kind\n"),
    row("insert into movement values(null,'abcdefghijklm','2026-01-05','receipt',5,200);", "balance", "error: bad sku\n"),
    row("insert into movement values(null,'a','2026-02-30','receipt',5,200);", "balance", "error: bad day\n"),
    row("insert into movement values(null,'a','2026-1-1','receipt',5,200);", "balance", "error: bad day\n"),
    row("insert into movement values(null,'a','1969-12-31','receipt',5,200);", "balance", "error: bad day\n"),
    row("insert into movement values(null,'a','2024-02-29','receipt',1000000,0);", "balance", "a|1000000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',1000001,200);", "balance", "error: bad quantity\n"),
    row("insert into movement values(null,'a','2026-01-05','issue','many',null);", "balance", "error: bad quantity\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,null);", "balance", "error: receipt needs unit_cents\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,-1);", "balance", "error: bad unit_cents\n"),
    row("insert into movement values(null,'a','2026-01-05','scrap',5,200);", "balance", "error: only receipts have unit_cents\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,200); update movement set qty = qty + 1;", "balance", "error: movements are append-only\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,200); delete from movement;", "balance", "error: movements are append-only\n"),
    row("insert into item values('a','Apple',-1);", "balance", "error: bad reorder_level\n"),
    row("insert into setting values('as_of','2026-02-30');", "balance", "error: bad as_of\n"),
    row("insert into setting values('cover_window','030');", "balance", "error: bad cover_window\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
