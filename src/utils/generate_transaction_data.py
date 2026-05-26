from faker import Faker
import pandas as pd
import random
import json
import os
from datetime import datetime

fake = Faker()

os.makedirs("data/streaming", exist_ok=True)

# -------------------------
# Generate Orders
# -------------------------

orders = []

for i in range(1, 1001):

    order = {
        "order_id": i,
        "customer_id": random.randint(1, 200),
        "product_id": random.randint(1, 100),
        "quantity": random.randint(1, 5),
        "order_amount": round(random.uniform(20, 1000), 2),
        "order_status": random.choice([
            "PLACED",
            "SHIPPED",
            "DELIVERED",
            "CANCELLED"
        ]),
        "order_timestamp": datetime.now().isoformat()
    }

    orders.append(order)

# Write Orders JSON
with open("data/streaming/orders.json", "w") as f:
    for order in orders:
        json.dump(order, f)
        f.write("\n")

# -------------------------
# Generate Payments
# -------------------------

payments = []

for i in range(1, 1001):

    payment = {
        "payment_id": i,
        "order_id": random.randint(1, 1000),
        "payment_method": random.choice([
            "UPI",
            "CARD",
            "NET_BANKING",
            "WALLET"
        ]),
        "payment_status": random.choice([
            "SUCCESS",
            "FAILED",
            "PENDING"
        ]),
        "payment_amount": round(random.uniform(20, 1000), 2),
        "payment_timestamp": datetime.now().isoformat()
    }

    payments.append(payment)

# Write Payments JSON
with open("data/streaming/payments.json", "w") as f:
    for payment in payments:
        json.dump(payment, f)
        f.write("\n")

print("Transaction data generated successfully.")