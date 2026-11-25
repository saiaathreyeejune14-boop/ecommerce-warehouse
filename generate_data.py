import os, random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")          # Indian names and cities
Faker.seed(42)                 # same data every time you run it
random.seed(42)
os.makedirs("data", exist_ok=True)

# --- Customers: who buys ---
customers = []
for i in range(1, 201):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "signup_date": fake.date_between("-2y", "-1y"),
    })

# --- Products: what is sold ---
categories = {"Electronics": (5000, 60000), "Clothing": (300, 3000),
              "Home": (500, 8000), "Books": (150, 1200), "Sports": (400, 10000)}
products = []
for i in range(1, 51):
    cat = random.choice(list(categories))
    low, high = categories[cat]
    products.append({
        "product_id": i,
        "product_name": f"{fake.word().title()} {cat}",
        "category": cat,
        "price": round(random.uniform(low, high), 2),
    })

# --- Orders: the sales events ---
orders = []
for i in range(1, 1001):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 200),
        "product_id": random.randint(1, 50),
        "order_date": fake.date_between("-1y", "today"),
        "quantity": random.randint(1, 5),
        "status": random.choice(["completed"] * 8 + ["cancelled", "returned"]),
    })

# --- Add some real-world mess for us to clean later ---
for c in random.sample(customers, 10):
    c["email"] = "  " + c["email"].upper() + " "   # messy emails
orders += random.sample(orders, 5)                  # 5 duplicate orders

pd.DataFrame(customers).to_csv("data/customers.csv", index=False)
pd.DataFrame(products).to_csv("data/products.csv", index=False)
pd.DataFrame(orders).to_csv("data/orders.csv", index=False)
print(f"Created {len(customers)} customers, {len(products)} products, {len(orders)} orders")