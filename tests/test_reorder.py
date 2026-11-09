from harness import row, rows_test

# fmt: off
ROWS = [
    row("insert into item values('a','Apple',5); insert into movement values(null,'a','2026-01-05','receipt',3,1);", "reorder", "a|Apple|3|5|2\n"),
    row("insert into item values('a','Apple',5); insert into movement values(null,'a','2026-01-05','receipt',5,1);", "reorder", ""),
    row("insert into item values('b','Bolt',2),('a','Apple',0),('c','Cog',1); insert into movement values(null,'a','2026-01-05','receipt',1,1),(null,'a','2026-01-06','issue',1,null);", "reorder", "b|Bolt|0|2|2\nc|Cog|0|1|1\n"),
    row("insert into item values('a','Apple',5); insert into movement values(null,'a','2026-01-05','receipt',2,1),(null,'a','2026-01-06','issue',4,null);", "reorder", "a|Apple|-2|5|7\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,1),(null,'a','2026-01-20','issue',6,null),(null,'a','2026-01-25','issue',4,null); insert into setting values('as_of','2026-02-04');", "cover", ""),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,1),(null,'a','2026-01-20','issue',6,null); insert into setting values('as_of','2026-02-04'),('cover_window','10');", "cover", "a|4|0|NULL\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,1),(null,'a','2026-01-05','issue',2,null),(null,'a','2026-01-10','scrap',3,null); insert into setting values('as_of','2026-01-31');", "cover", "a|5|2|75\n"),
    row("insert into movement values(null,'a','2026-01-05','receipt',10,1),(null,'a','2026-01-20','issue',6,null);", "cover", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
