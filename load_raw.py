import pandas as pd
from sqlalchemy import create_engine, text, inspect

engine = create_engine("postgresql+psycopg://postgres:pass@localhost:5432/postgres")

# A separate "folder" in the database for untouched source data
with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))

for name in ["customers", "products", "orders"]:
    # dtype=str: load everything as text, exactly as in the file
    df = pd.read_csv(f"data/{name}.csv", dtype=str)

    # Empty the table if it exists (don't drop: dbt views will depend on it)
    if inspect(engine).has_table(name, schema="raw"):
        with engine.begin() as conn:
            conn.execute(text(f"TRUNCATE raw.{name}"))

    df.to_sql(name, engine, schema="raw", if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into raw.{name}")