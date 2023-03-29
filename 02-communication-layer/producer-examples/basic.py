import datetime
from .producer_helper import Producer

# Create a producer instance
redpanda_producer = Producer(topic="purchases")

# Write a purchase event to Redpanda
message = {
    "user_id": 100001,
    "product_id": 200002,
    "event_type": "purchase",
    "product_name": "Mario Odyssey (Switch Game)",
    "qty": 1,
    "unit_price": 39.99,
    "event_timestamp": int(datetime.datetime(2023, 3, 10).timestamp() * 1000),
}

redpanda_producer.produce(value=message)
