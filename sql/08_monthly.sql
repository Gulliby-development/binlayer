create view monthly as
select
    substr(day, 1, 7) as month,
    sku,
    sum(case when kind = 'issue' then qty else 0 end) as issued,
    sum(case when kind = 'scrap' then qty else 0 end) as scrapped,
    sum(case when kind = 'issue' then cost_cents else 0 end) as cogs_cents,
    sum(case when kind = 'scrap' then cost_cents else 0 end) as scrap_cents
from issue_cost
group by substr(day, 1, 7), sku;

create view month_total as
with monthly_costs as (
    select
        month,
        sum(cogs_cents) as cogs_cents
    from monthly
    group by month
)

select
    month,
    cogs_cents,
    sum(cogs_cents) over (
        order by month
        rows between unbounded preceding and current row
    ) as running_cents
from monthly_costs;
