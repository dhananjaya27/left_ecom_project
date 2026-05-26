from faker import Faker
import random
import json
import os
import time

fake = Faker()

os.makedirs("data/cdc", exist_ok=True)

cdc_events = []

operations = ["c", "u", "d"]

for i in range(1, 201):

    op = random.choice(operations)

    before_data = {
        "customer_id": i,
        "customer_name": fake.name(),
        "email": fake.email(),
        "city": fake.city()
    }

    after_data = {
        "customer_id": i,
        "customer_name": fake.name(),
        "email": fake.email(),
        "city": fake.city()
    }

    event = {
        "before": before_data if op in ["u", "d"] else None,
        "after": after_data if op in ["c", "u"] else None,
        "op": op,
        "ts_ms": int(time.time() * 1000)
    }

    cdc_events.append(event)

# Write CDC JSON
with open("data/cdc/customer_cdc.json", "w") as f:
    for event in cdc_events:
        json.dump(event, f)
        f.write("\n")

print("CDC events generated successfully.")
