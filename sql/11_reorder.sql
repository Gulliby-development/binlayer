create view reorder (sku, name, on_hand, reorder_level, short) as
select
    item.sku,
    item.name,
    coalesce(balance.on_hand, 0) as on_hand,
    item.reorder_level,
    item.reorder_level - coalesce(balance.on_hand, 0) as short
from item
left join balance on balance.sku = item.sku
where coalesce(balance.on_hand, 0) < item.reorder_level;

create view cover (sku, on_hand, used, cover_days) as
with params as (
    select
        asof_setting.val as as_of,
        coalesce(
            (
                select cast(window_setting.val as integer)
                from setting as window_setting
                where window_setting.name = 'cover_window'
            ),
            30
        ) as window_days
    from setting as asof_setting
    where asof_setting.name = 'as_of'
),

usage as (
    select
        balance.sku,
        balance.on_hand,
        params.window_days,
        coalesce(sum(movement.qty), 0) as used
    from balance
    cross join params
    left join movement
        on
            movement.sku = balance.sku
            and movement.kind = 'issue'
            and movement.day > date(params.as_of, '-' || params.window_days || ' days')
            and movement.day <= params.as_of
    where balance.on_hand > 0
    group by balance.sku, balance.on_hand, params.window_days
)

select
    sku,
    on_hand,
    used,
    case when used = 0 then null else on_hand * window_days / used end as cover_days
from usage;
