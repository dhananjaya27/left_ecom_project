from faker import Faker
import random
import json
import os
from datetime import datetime

fake = Faker()

# Create logs directory
os.makedirs("data/logs", exist_ok=True)

clickstream_events = []

event_types = [
    "PAGE_VIEW",
    "SEARCH",
    "ADD_TO_CART",
    "CHECKOUT",
    "LOGIN",
    "LOGOUT"
]

device_types = [
    "mobile",
    "desktop",
    "tablet"
]

for i in range(1, 1001):

    event = {
        "event_id": i,
        "customer_id": random.randint(1, 200),
        "event_type": random.choice(event_types),
        "page_url": fake.uri_path(),
        "device_type": random.choice(device_types),
        "ip_address": fake.ipv4(),
        "session_id": fake.uuid4(),
        "event_timestamp": datetime.now().isoformat()
    }

    clickstream_events.append(event)

# Write JSON logs
with open("data/logs/clickstream_logs.json", "w") as f:
    for event in clickstream_events:
        json.dump(event, f)
        f.write("\n")

print("Clickstream logs generated successfully.")