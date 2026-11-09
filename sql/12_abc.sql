create view abc as
with ranked as (
    select
        row_number() over (order by value_cents desc, sku asc) as pos,
        sku,
        value_cents,
        sum(value_cents) over () as total_value,
        coalesce(
            sum(value_cents) over (
                order by value_cents desc, sku asc
                rows between unbounded preceding and 1 preceding
            ),
            0
        ) as preceding_value
    from stock_value
)

select
    pos,
    sku,
    value_cents,
    case
        when preceding_value * 100 < 80 * total_value then 'A'
        when preceding_value * 100 < 95 * total_value then 'B'
        else 'C'
    end as class
from ranked;
