from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null);", "issue_cost", "2|a|2026-01-06|issue|4|4|800\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-07','receipt',5,300),(null,'a','2026-01-09','issue',12,null),(null,'a','2026-01-10','scrap',2,null);", "issue_cost", "3|a|2026-01-09|issue|12|12|2600\n4|a|2026-01-10|scrap|2|2|600\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',4,0),(null,'a','2026-01-06','issue',4,null);", "issue_cost", "2|a|2026-01-06|issue|4|4|0\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',6,33),(null,'a','2026-01-06','issue',1,null),(null,'a','2026-01-06','issue',1,null),(null,'a','2026-01-06','issue',1,null);", "issue_cost", "2|a|2026-01-06|issue|1|1|33\n3|a|2026-01-06|issue|1|1|33\n4|a|2026-01-06|issue|1|1|33\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',9,10),(null,'a','2026-01-06','receipt',9,20),(null,'a','2026-01-06','issue',10,null);", "issue_cost", "3|a|2026-01-06|issue|10|10|110\n"),
    row("insert into movement values(null,'a','2026-01-31','receipt',3,10),(null,'a','2026-02-01','issue',1,null),(null,'a','2026-02-01','issue',1,null);", "issue_cost", "2|a|2026-02-01|issue|1|1|10\n3|a|2026-02-01|issue|1|1|10\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',1000000,100000000),(null,'a','2026-01-06','issue',1000000,null);", "issue_cost", "2|a|2026-01-06|issue|1000000|1000000|100000000000000\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',2,5);", "issue_cost", ""),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,11),(null,'a','2026-01-06','scrap',5,null);", "issue_cost", "2|a|2026-01-06|scrap|5|5|55\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
