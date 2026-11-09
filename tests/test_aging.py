from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200); insert into setting values('as_of','2026-01-05');", "aging", "a|0-30|10|2000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200); insert into setting values('as_of','2026-02-04');", "aging", "a|0-30|10|2000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200); insert into setting values('as_of','2026-02-05');", "aging", "a|31-60|10|2000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200); insert into setting values('as_of','2026-03-06');", "aging", "a|31-60|10|2000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200); insert into setting values('as_of','2026-03-07');", "aging", "a|61+|10|2000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-03-20','receipt',4,5); insert into setting values('as_of','2026-03-10');", "aging", "a|61+|10|2000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200);", "aging", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
