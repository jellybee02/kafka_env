import asyncio
import json
from confluent_kafka import Consumer
from app.db import SessionLocal
from app.models import Order

consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',  # 도커 바깥에서 실행할 때만
    'group.id': 'order-consumers',
    'auto.offset.reset': 'earliest'
})

async def consume():
    consumer.subscribe(['order-events'])
    print("Kafka Consumer started...")

    while True:
        msg = consumer.poll(1.0)
        if msg is None or msg.error():
            await asyncio.sleep(1)
            continue
        data = json.loads(msg.value().decode('utf-8'))

        async with SessionLocal() as session:
            order = Order(**data)
            session.add(order)
            await session.commit()

if __name__ == "__main__":
    asyncio.run(consume())
