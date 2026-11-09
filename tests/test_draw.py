from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null);", "draw", "2|1|4|200|800\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-07','receipt',5,300),(null,'a','2026-01-09','issue',12,null);", "draw", "3|1|10|200|2000\n3|2|2|300|600\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-07','receipt',5,300),(null,'a','2026-01-09','issue',10,null),(null,'a','2026-01-10','issue',5,null);", "draw", "3|1|10|200|2000\n4|2|5|300|1500\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',3,10),(null,'a','2026-01-06','receipt',3,20),(null,'a','2026-01-07','receipt',3,30),(null,'a','2026-01-08','issue',8,null);", "draw", "4|1|3|10|30\n4|2|3|20|60\n4|3|2|30|60\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,0),(null,'a','2026-01-06','receipt',5,7),(null,'a','2026-01-07','issue',6,null);", "draw", "3|1|5|0|0\n3|2|1|7|7\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'a','2026-01-06','issue',2,null),(null,'a','2026-01-07','scrap',2,null),(null,'a','2026-01-08','issue',1,null);", "draw", "2|1|2|100|200\n3|1|2|100|200\n4|1|1|100|100\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'b','2026-01-05','receipt',5,900),(null,'b','2026-01-06','issue',4,null),(null,'a','2026-01-06','issue',1,null);", "draw", "3|2|4|900|3600\n4|1|1|100|100\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'a','2026-01-08','receipt',5,500),(null,'a','2026-01-09','issue',7,null),(null,'a','2026-01-06','issue',3,null);", "draw", "3|1|2|100|200\n3|2|5|500|2500\n4|1|3|100|300\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',1000000,100000000),(null,'a','2026-01-06','issue',1000000,null);", "draw", "2|1|1000000|100000000|100000000000000\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
