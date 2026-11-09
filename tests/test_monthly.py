from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null);", "monthly", "2026-01|a|4|0|800|0\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null),(null,'a','2026-01-07','scrap',2,null),(null,'a','2026-01-31','issue',1,null);", "monthly", "2026-01|a|5|2|1000|400\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-31','issue',4,null),(null,'a','2026-02-01','issue',4,null);", "monthly", "2026-01|a|4|0|800|0\n2026-02|a|4|0|800|0\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,100),(null,'b','2026-01-05','receipt',10,300),(null,'b','2026-02-02','issue',1,null),(null,'a','2026-02-02','issue',2,null),(null,'b','2026-02-03','scrap',2,null);", "monthly", "2026-02|a|2|0|200|0\n2026-02|b|1|2|300|600\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,100),(null,'b','2026-01-05','receipt',10,300),(null,'b','2026-01-10','issue',1,null),(null,'a','2026-01-11','issue',2,null),(null,'b','2026-03-03','issue',2,null),(null,'a','2026-03-04','scrap',1,null);", "month_total", "2026-01|500|500\n2026-03|600|1100\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,100),(null,'a','2026-02-06','issue',4,null),(null,'a','2026-04-07','issue',4,null);", "month_total", "2026-02|400|400\n2026-04|400|800\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,100),(null,'a','2026-01-06','scrap',4,null);", "month_total", "2026-01|0|0\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
