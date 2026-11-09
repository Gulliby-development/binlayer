from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1);", "calendar", "2026-01-05\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1),(null,'a','2026-01-08','issue',1,null);", "calendar", "2026-01-05\n2026-01-06\n2026-01-07\n2026-01-08\n"),
    row("insert into movement values(null,'a','2026-02-27','receipt',5,1),(null,'a','2026-03-02','issue',1,null);", "calendar", "2026-02-27\n2026-02-28\n2026-03-01\n2026-03-02\n"),
    row("insert into movement values(null,'a','2024-02-27','receipt',5,1),(null,'a','2024-03-01','issue',1,null);", "calendar", "2024-02-27\n2024-02-28\n2024-02-29\n2024-03-01\n"),
    row("insert into movement values(null,'a','2026-12-30','receipt',5,1),(null,'a','2027-01-02','issue',1,null);", "calendar", "2026-12-30\n2026-12-31\n2027-01-01\n2027-01-02\n"),
    row("", "calendar", ""),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1),(null,'a','2026-01-08','issue',2,null);", "daily", "a|2026-01-05|5\na|2026-01-06|5\na|2026-01-07|5\na|2026-01-08|3\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,1),(null,'a','2026-01-06','issue',6,null),(null,'a','2026-01-07','receipt',2,1);", "daily", "a|2026-01-05|5\na|2026-01-06|-1\na|2026-01-07|1\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
