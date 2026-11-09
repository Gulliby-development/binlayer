create view layer_left as
with take_totals as (
    select
        sku,
        sum(qty) as total_taken
    from take
    group by sku
)

select
    layer.receipt_id,
    layer.sku,
    layer.last_pos - max(layer.first_pos, coalesce(take_totals.total_taken, 0)) as left_qty,
    layer.unit_cents,
    (layer.last_pos - max(layer.first_pos, coalesce(take_totals.total_taken, 0)))
    * layer.unit_cents as value_cents
from layer
left join take_totals on take_totals.sku = layer.sku
where layer.last_pos - max(layer.first_pos, coalesce(take_totals.total_taken, 0)) > 0;

create view stock_value as
select
    sku,
    sum(left_qty) as on_hand,
    sum(value_cents) as value_cents
from layer_left
group by sku;

create view avg_cost as
select
    sku,
    on_hand,
    (2 * value_cents + on_hand) / (2 * on_hand) as avg_cents
from stock_value;
