create view calendar (day) as
with recursive
bounds (first_day, last_day) as (
    select
        min(day),
        max(day)
    from movement
),

calendar_days (day, last_day) as (
    select
        first_day,
        last_day
    from bounds
    where first_day is not null

    union all

    select
        date(day, '+1 day'),
        last_day
    from calendar_days
    where day < last_day
)

select day
from calendar_days;

create view daily (sku, day, on_hand) as
with
sku_starts (sku, first_day) as (
    select
        sku,
        min(day)
    from movement
    group by sku
),

daily_deltas (sku, day, delta) as (
    select
        sku,
        day,
        sum(case when kind = 'receipt' then qty else -qty end) as delta
    from movement
    group by sku, day
),

daily_rows (sku, day, delta) as (
    select
        sku_starts.sku,
        calendar.day,
        coalesce(daily_deltas.delta, 0) as delta
    from sku_starts
    inner join calendar on calendar.day >= sku_starts.first_day
    left join daily_deltas
        on
            daily_deltas.sku = sku_starts.sku
            and daily_deltas.day = calendar.day
)

select
    sku,
    day,
    sum(delta) over (
        partition by sku
        order by day
        rows between unbounded preceding and current row
    ) as on_hand
from daily_rows;

create view empty_spans (sku, start_day, end_day, days) as
with
zero_days (sku, day, prior_day) as (
    select
        sku,
        day,
        lag(day) over (partition by sku order by day) as prior_day
    from daily
    where on_hand = 0
),

island_starts (sku, day, starts_island) as (
    select
        sku,
        day,
        case
            when prior_day = date(day, '-1 day') then 0
            else 1
        end as starts_island
    from zero_days
),

island_days (sku, day, island) as (
    select
        sku,
        day,
        sum(starts_island) over (
            partition by sku
            order by day
            rows between unbounded preceding and current row
        ) as island
    from island_starts
)

select
    sku,
    min(day) as start_day,
    max(day) as end_day,
    count(*) as days
from island_days
group by sku, island;
