select
    o.order_id,
    o.customer_id,
    o.product_id,
    o.order_date,
    o.status,
    o.quantity,
    p.price               as unit_price,
    o.quantity * p.price  as revenue
from {{ ref('stg_orders') }} o
join {{ ref('stg_products') }} p on o.product_id = p.product_id