with deduped as (
    select distinct * from {{ source('raw', 'orders') }}
)

select
    cast(order_id as int)     as order_id,
    cast(customer_id as int)  as customer_id,
    cast(product_id as int)   as product_id,
    cast(order_date as date)  as order_date,
    cast(quantity as int)     as quantity,
    lower(trim(status))       as status
from deduped