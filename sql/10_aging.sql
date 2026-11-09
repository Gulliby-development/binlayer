create view aging as
with as_of_day as (
    select val as day
    from setting
    where name = 'as_of'
),

layer_ages as (
    select
        layer_left.sku,
        layer_left.left_qty,
        layer_left.value_cents,
        cast(julianday(as_of_day.day) - julianday(movement.day) as integer) as age_days
    from layer_left
    inner join movement on movement.id = layer_left.receipt_id
    cross join as_of_day
    where movement.day <= as_of_day.day
)

select
    sku,
    case
        when age_days <= 30 then '0-30'
        when age_days <= 60 then '31-60'
        else '61+'
    end as bucket,
    sum(left_qty) as qty,
    sum(value_cents) as value_cents
from layer_ages
group by sku, bucket;
