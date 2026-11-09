from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',2,5);", "avg_cost", "a|2|5\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',3,1);", "avg_cost", "a|3|1\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',1,3),(null,'a','2026-01-06','receipt',1,2);", "avg_cost", "a|2|3\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',3,10),(null,'a','2026-01-06','receipt',3,11);", "avg_cost", "a|6|11\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',4,25),(null,'a','2026-01-06','receipt',4,26),(null,'a','2026-01-07','issue',4,null);", "avg_cost", "a|4|26\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,0),(null,'b','2026-01-05','receipt',3,7),(null,'b','2026-01-06','receipt',1,8);", "avg_cost", "a|5|0\nb|4|7\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',999999,100000000),(null,'a','2026-01-06','receipt',1,99999999);", "avg_cost", "a|1000000|100000000\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
