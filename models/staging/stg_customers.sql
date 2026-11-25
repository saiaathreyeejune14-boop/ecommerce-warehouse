select
    cast(customer_id as int)   as customer_id,
    trim(name)                 as customer_name,
    lower(trim(email))         as email,
    trim(city)                 as city,
    cast(signup_date as date)  as signup_date
from {{ source('raw', 'customers') }}