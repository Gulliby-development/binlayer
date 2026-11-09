from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1),(null,'a','2026-01-08','issue',5,null),(null,'a','2026-01-10','receipt',2,1);", "empty_spans", "a|2026-01-08|2026-01-09|2\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1),(null,'a','2026-01-08','issue',5,null),(null,'b','2026-01-12','receipt',1,1);", "empty_spans", "a|2026-01-08|2026-01-12|5\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1),(null,'a','2026-01-06','issue',5,null),(null,'a','2026-01-08','receipt',5,1),(null,'a','2026-01-09','scrap',5,null),(null,'b','2026-01-12','receipt',1,1);", "empty_spans", "a|2026-01-06|2026-01-07|2\na|2026-01-09|2026-01-12|4\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1);", "empty_spans", ""),
    row("insert into movement values(null,'a','2026-01-30','receipt',5,1),(null,'a','2026-01-31','issue',5,null),(null,'b','2026-02-03','receipt',1,1);", "empty_spans", "a|2026-01-31|2026-02-03|4\n"),
    row("insert into movement values(null,'a','2026-12-30','receipt',1,1),(null,'a','2026-12-30','issue',1,null),(null,'b','2027-01-02','receipt',1,1);", "empty_spans", "a|2026-12-30|2027-01-02|4\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1),(null,'a','2026-01-06','issue',3,null),(null,'a','2026-01-06','issue',2,null),(null,'b','2026-01-08','receipt',1,1);", "empty_spans", "a|2026-01-06|2026-01-08|3\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
