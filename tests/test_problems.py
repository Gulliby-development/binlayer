from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into item values('a','Apple',0); insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'a','2026-01-06','issue',5,null);", "problems", ""),
    row("insert into item values('a','Apple',0); insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'a','2026-01-06','issue',6,null);", "problems", "2|a|2026-01-06|short\n"),
    row("insert into item values('a','Apple',0); insert into movement values(null,'a','2026-01-05','receipt',5,100),(null,'a','2026-01-06','issue',3,null),(null,'a','2026-01-07','issue',3,null),(null,'a','2026-01-08','scrap',1,null);", "problems", "3|a|2026-01-07|short\n4|a|2026-01-08|short\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',5,100);", "problems", "1|a|2026-01-05|no item\n"),
    row("insert into item values('a','Apple',0),('b','Bolt',0); insert into movement values(null,'b','2026-01-05','receipt',1,1),(null,'a','2026-01-05','receipt',1,1),(null,'c','2026-01-04','receipt',1,1),(null,'c','2026-01-06','receipt',1,1);", "problems", "3|c|2026-01-04|no item\n"),
    row("insert into item values('a','Apple',0); insert into movement values(null,'a','2026-01-05','issue',1,null),(null,'a','2026-01-04','receipt',5,10);", "problems", ""),
    row("insert into movement values(null,'z','2026-01-05','issue',1,null);", "problems", "1|z|2026-01-05|no item\n1|z|2026-01-05|short\n"),
    row("", "problems", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
