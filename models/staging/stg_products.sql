select
    cast(product_id as int)        as product_id,
    trim(product_name)             as product_name,
    trim(category)                 as category,
    cast(price as numeric(10, 2))  as price
from {{ source('raw', 'products') }}