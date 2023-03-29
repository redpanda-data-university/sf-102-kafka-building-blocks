import datetime
from .producer_helper import Producer

# Create a serializer that allows us to set string keys
config = {
    "key_serializer": str.encode,
}

# Create a producer instance
redpanda_producer = Producer(topic="purchases", producer_config=config)

# Write a purchase event to Redpanda
message = {
    "user_id": 300003,
    "product_id": 200002,
    "event_type": "purchase",
    "product_name": "Mario Odyssey (Switch Game)",
    "qty": 1,
    "unit_price": 39.99,
    "event_timestamp": int(datetime.datetime(2023, 3, 10).timestamp() * 1000),
}

# with key and timestamp
redpanda_producer.produce(
    key=str(message.get("user_id")),
    timestamp_ms=message.get("event_timestamp"),
    value=message,
)
