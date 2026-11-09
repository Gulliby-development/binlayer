create view balance (sku, on_hand) as
select
    sku,
    sum(case when kind = 'receipt' then qty else -qty end) as on_hand
from movement
group by sku;

create view running (id, sku, day, kind, qty, on_hand) as
select
    id,
    sku,
    day,
    kind,
    qty,
    sum(case when kind = 'receipt' then qty else -qty end) over (
        partition by sku
        order by day, id
        rows between unbounded preceding and current row
    ) as on_hand
from movement;
