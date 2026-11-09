from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200);", "balance", "a|10\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null),(null,'a','2026-01-07','scrap',1,null);", "balance", "a|5\n"),
    row("insert into movement values(null,'b','2026-01-05','receipt',3,1),(null,'a-1','2026-01-05','receipt',2,1),(null,'a1','2026-01-05','receipt',1,1),(null,'9','2026-01-05','receipt',7,1);", "balance", "9|7\na-1|2\na1|1\nb|3\n"),
    row("", "balance", ""),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',10,null);", "balance", "a|0\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null),(null,'a','2026-01-07','scrap',1,null);", "running", "1|a|2026-01-05|receipt|10|10\n2|a|2026-01-06|issue|4|6\n3|a|2026-01-07|scrap|1|5\n"),
    row("insert into movement values(null,'a','2026-01-09','issue',2,null),(null,'a','2026-01-05','receipt',5,100);", "running", "2|a|2026-01-05|receipt|5|5\n1|a|2026-01-09|issue|2|3\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'b','2026-01-05','receipt',8,100),(null,'a','2026-01-05','issue',2,null),(null,'b','2026-01-06','issue',8,null);", "running", "1|a|2026-01-05|receipt|5|5\n3|a|2026-01-05|issue|2|3\n2|b|2026-01-05|receipt|8|8\n4|b|2026-01-06|issue|8|0\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'a','2026-01-05','issue',7,null),(null,'a','2026-01-05','receipt',9,100);", "running", "1|a|2026-01-05|receipt|5|5\n2|a|2026-01-05|issue|7|-2\n3|a|2026-01-05|receipt|9|7\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
