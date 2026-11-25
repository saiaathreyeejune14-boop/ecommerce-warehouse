select
    d.year,
    d.month,
    d.month_name,
    count(*)            as orders,
    sum(f.revenue)      as revenue
from {{ ref('fct_orders') }} f
join {{ ref('dim_date') }} d on f.order_date = d.date_day
where f.status = 'completed'
group by d.year, d.month, d.month_name
order by d.year, d.month