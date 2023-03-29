import json
import os

from kafka import KafkaConsumer

# Create a consumer client
consumer = KafkaConsumer(
    # topic
    "purchases",
    # consumer configs
    bootstrap_servers=os.getenv("REDPANDA_BROKERS", ""),
    group_id="my-group",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v),
)

# Consume messages from a Redpanda topic
for msg in consumer:
    print(f"Consumed record. key={msg.key}, value={msg.value}")
