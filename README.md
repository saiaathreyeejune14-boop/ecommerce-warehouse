\# E-commerce Sales Warehouse



A dbt data warehouse that models e-commerce sales data as a star schema.



\## Architecture

CSV files -> Python (raw load) -> Postgres -> dbt staging -> star schema -> business metrics



\## Data model

\- fct\_orders: one row per order, with revenue

\- dim\_customers, dim\_products, dim\_date: who, what and when

\- mart\_monthly\_revenue, mart\_top\_products, mart\_city\_revenue: business metrics



\## What it shows

\- Cleaning messy data (emails, duplicates, data types) in staging

\- Star schema design with fact and dimension tables

\- dbt tests: unique, not\_null, relationships, accepted\_values

\- dbt docs with lineage graph



\## How to run

1\. docker start pg

2\. python generate\_data.py

3\. python load\_raw.py

4\. dbt run

5\. dbt test

