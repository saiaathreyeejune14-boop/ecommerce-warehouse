select
    d::date                          as date_day,
    extract(year from d)::int        as year,
    extract(month from d)::int       as month,
    to_char(d, 'Mon')                as month_name,
    extract(quarter from d)::int     as quarter,
    trim(to_char(d, 'Day'))          as day_name,
    extract(isodow from d) in (6, 7) as is_weekend
from generate_series(
    (select min(order_date) from {{ ref('stg_orders') }}),
    (select max(order_date) from {{ ref('stg_orders') }}),
    interval '1 day'
) as d