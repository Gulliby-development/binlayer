create view problems (id, sku, day, problem) as
select
    id,
    sku,
    day,
    'short' as problem
from running
where on_hand < 0

union all

select
    movement.id,
    movement.sku,
    movement.day,
    'no item' as problem
from movement
left join item on movement.sku = item.sku
where
    item.sku is null
    and movement.id = (
        select min(first_movement.id)
        from movement as first_movement
        where first_movement.sku = movement.sku
    );
