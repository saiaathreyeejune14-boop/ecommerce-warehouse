select
    p.product_name,
    p.category,
    sum(f.quantity)  as units_sold,
    sum(f.revenue)   as revenue
from {{ ref('fct_orders') }} f
join {{ ref('dim_products') }} p on f.product_id = p.product_id
where f.status = 'completed'
group by p.product_name, p.category
order by revenue desc