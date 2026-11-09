create view layer as
with receipts as (
    select
        id as receipt_id,
        sku,
        day,
        qty,
        unit_cents
    from movement
    where kind = 'receipt'
),

positioned_receipts as (
    select
        receipt_id,
        sku,
        day,
        qty,
        unit_cents,
        sum(qty) over (
            partition by sku
            order by day, receipt_id
            rows between unbounded preceding and current row
        ) - qty as first_pos,
        sum(qty) over (
            partition by sku
            order by day, receipt_id
            rows between unbounded preceding and current row
        ) as last_pos
    from receipts
)

select
    receipt_id,
    sku,
    day,
    qty,
    unit_cents,
    first_pos,
    last_pos
from positioned_receipts;

create view take as
with takes as (
    select
        id as issue_id,
        sku,
        day,
        kind,
        qty
    from movement
    where kind in ('issue', 'scrap')
),

positioned_takes as (
    select
        issue_id,
        sku,
        day,
        kind,
        qty,
        sum(qty) over (
            partition by sku
            order by day, issue_id
            rows between unbounded preceding and current row
        ) - qty as from_pos,
        sum(qty) over (
            partition by sku
            order by day, issue_id
            rows between unbounded preceding and current row
        ) as to_pos
    from takes
)

select
    issue_id,
    sku,
    day,
    kind,
    qty,
    from_pos,
    to_pos
from positioned_takes;

create view draw as
select
    take.issue_id,
    layer.receipt_id,
    min(take.to_pos, layer.last_pos) - max(take.from_pos, layer.first_pos) as qty,
    layer.unit_cents,
    (min(take.to_pos, layer.last_pos) - max(take.from_pos, layer.first_pos))
    * layer.unit_cents as cost_cents
from take
inner join layer on layer.sku = take.sku
where min(take.to_pos, layer.last_pos) - max(take.from_pos, layer.first_pos) > 0;
