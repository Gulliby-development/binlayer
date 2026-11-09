from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null);", "layer_left", "1|a|6|200|1200\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-07','receipt',5,300),(null,'a','2026-01-09','issue',12,null);", "layer_left", "2|a|3|300|900\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-07','receipt',5,300),(null,'a','2026-01-09','issue',10,null);", "layer_left", "2|a|5|300|1500\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',10,null);", "layer_left", ""),
    row("insert into movement values(null,'a','2026-01-05','receipt',3,1),(null,'b','2026-01-05','receipt',2,4),(null,'b','2026-01-06','receipt',2,5),(null,'b','2026-01-07','scrap',3,null);", "layer_left", "1|a|3|1|3\n3|b|1|5|5\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null);", "stock_value", "a|6|1200\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-07','receipt',5,300),(null,'a','2026-01-09','issue',12,null),(null,'b','2026-01-05','receipt',7,0);", "stock_value", "a|3|900\nb|7|0\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',10,null),(null,'b','2026-01-05','receipt',1,1);", "stock_value", "b|1|1\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',1000000,100000000);", "stock_value", "a|1000000|100000000000000\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
