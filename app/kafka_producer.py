import os
from confluent_kafka import Producer
import json
import asyncio

producer = Producer({'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS")})

async def send_order_event(data: dict):
    producer.produce("order-events", json.dumps(data).encode("utf-8"))
    producer.flush()
    await asyncio.sleep(0.1)
