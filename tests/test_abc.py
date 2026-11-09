from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into movement values(null,'a','2026-01-05','receipt',1,100);", "abc", "1|a|100|A\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',8,10),(null,'b','2026-01-05','receipt',1,10),(null,'c','2026-01-05','receipt',1,10);", "abc", "1|a|80|A\n2|b|10|B\n3|c|10|B\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',1,80),(null,'b','2026-01-05','receipt',1,15),(null,'c','2026-01-05','receipt',1,5);", "abc", "1|a|80|A\n2|b|15|B\n3|c|5|C\n"),
    row("insert into movement values(null,'b','2026-01-05','receipt',1,40),(null,'a','2026-01-05','receipt',1,40),(null,'c','2026-01-05','receipt',1,20);", "abc", "1|a|40|A\n2|b|40|A\n3|c|20|B\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',3,0),(null,'b','2026-01-05','receipt',2,0);", "abc", "1|a|0|C\n2|b|0|C\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',2,100),(null,'a','2026-01-06','issue',1,null),(null,'b','2026-01-05','receipt',1,99),(null,'c','2026-01-05','receipt',1,1);", "abc", "1|a|100|A\n2|b|99|A\n3|c|1|C\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
