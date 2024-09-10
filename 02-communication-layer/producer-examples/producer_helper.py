from kafka import KafkaProducer
import json
import os


class Producer:
    def __init__(self, topic, producer_config=None):
        if not producer_config:
            producer_config = {}
        # Define default values for KafkaProducer configuration
        defaults = {
            # Use a JSON serializer by default
            "bootstrap_servers": os.getenv("REDPANDA_BROKERS", "localhost:9092"),
            "value_serializer": lambda v: json.dumps(v).encode("utf-8"),
        }
        
        # Merge the default values with the provided configuration
        config = {**defaults, **producer_config}

        # Instantiate a Kafka producer client using the merged configuration.
        self.client = KafkaProducer(**config)
        self.topic = topic

    def produce(self, **kwargs):
        """Produce a single message to a Redpanda topic"""
        try:
            # Send a message to the topic
            future = self.client.send(self.topic, **kwargs)

            # Block until the message is sent (or timeout).
            _ = future.get(timeout=10)
            print(f"Successfully produced message to topic: {self.topic}")
        except Exception as e:
            print(f"Could not produce to topic: {self.topic}")
            raise
