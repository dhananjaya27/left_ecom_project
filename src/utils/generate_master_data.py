from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

# Create output directory
os.makedirs("data/raw", exist_ok=True)

# -------------------------
# Generate Products
# -------------------------

products = []

categories = [
    "Electronics",
    "Fashion",
    "Home",
    "Books",
    "Sports"
]

for i in range(1, 101):
    products.append({
        "product_id": i,
        "product_name": fake.word().title(),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 500), 2),
        "brand": fake.company(),
        "created_at": fake.date_time_this_year()
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

# -------------------------
# Generate Customers
# -------------------------

customers = []

for i in range(1, 201):
    customers.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state(),
        "country": fake.country(),
        "signup_date": fake.date_this_year()
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

# -------------------------
# Generate Vendors
# -------------------------

vendors = []

for i in range(1, 31):
    vendors.append({
        "vendor_id": i,
        "vendor_name": fake.company(),
        "country": fake.country(),
        "rating": round(random.uniform(1, 5), 1)
    })

vendors_df = pd.DataFrame(vendors)

vendors_df.to_csv(
    "data/raw/vendors.csv",
    index=False
)

print("Master data generated successfully.")