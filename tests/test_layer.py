from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200);", "layer", "1|a|2026-01-05|10|200|0|10\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-07','receipt',5,300),(null,'b','2026-01-06','receipt',4,50);", "layer", "1|a|2026-01-05|10|200|0|10\n2|a|2026-01-07|5|300|10|15\n3|b|2026-01-06|4|50|0|4\n"),
    row("insert into movement values(null,'a','2026-01-07','receipt',5,300),(null,'a','2026-01-05','receipt',10,200);", "layer", "2|a|2026-01-05|10|200|0|10\n1|a|2026-01-07|5|300|10|15\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',2,1),(null,'a','2026-01-05','receipt',3,2),(null,'a','2026-01-05','receipt',4,3);", "layer", "1|a|2026-01-05|2|1|0|2\n2|a|2026-01-05|3|2|2|5\n3|a|2026-01-05|4|3|5|9\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null);", "take", "2|a|2026-01-06|issue|4|0|4\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-06','issue',4,null),(null,'a','2026-01-07','scrap',3,null),(null,'a','2026-01-08','issue',2,null);", "take", "2|a|2026-01-06|issue|4|0|4\n3|a|2026-01-07|scrap|3|4|7\n4|a|2026-01-08|issue|2|7|9\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200),(null,'a','2026-01-08','issue',4,null),(null,'a','2026-01-06','issue',3,null);", "take", "2|a|2026-01-08|issue|4|3|7\n3|a|2026-01-06|issue|3|0|3\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,200);", "take", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
