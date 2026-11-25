select
    c.city,
    count(distinct c.customer_id)  as customers,
    sum(f.revenue)                 as revenue
from {{ ref('fct_orders') }} f
join {{ ref('dim_customers') }} c on f.customer_id = c.customer_id
where f.status = 'completed'
group by c.city
order by revenue desc