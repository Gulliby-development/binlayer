create view issue_cost as
with draw_totals as (
    select
        issue_id,
        sum(qty) as drawn,
        sum(cost_cents) as cost_cents
    from draw
    group by issue_id
)

select
    take.issue_id,
    take.sku,
    take.day,
    take.kind,
    take.qty,
    coalesce(draw_totals.drawn, 0) as drawn,
    coalesce(draw_totals.cost_cents, 0) as cost_cents
from take
left join draw_totals on draw_totals.issue_id = take.issue_id;
