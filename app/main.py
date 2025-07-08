from fastapi import FastAPI, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.kafka_producer import send_order_event
from app.db import SessionLocal
from app.models import Order
from sqlalchemy.future import select
from app.schemas import OrderIn

app = FastAPI()

# 주문 생성: Kafka로 전송
@app.post("/order")
async def create_order(order: OrderIn):
    await send_order_event(order.dict())
    return {"status": "Order event sent to Kafka"}
    # return {"status": "Order event sent to Kafka"}

# DB에 저장된 주문 목록 조회
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/orders")
async def get_orders(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order))
    return result.scalars().all()
# from fastapi import FastAPI
# from app.kafka_producer import send_order_event
# from app.schemas import OrderIn

# app = FastAPI()

# @app.post("/order")
# async def create_order(order: OrderIn):
#     await send_order_event(order.dict())
#     return {"status": "Order event sent to Kafka"}
