from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.kafka_producer import send_order_event
from app.db import SessionLocal
from app.models import Order
from app.schemas import OrderIn
from sqlalchemy.future import select

app = FastAPI()

# 주문 생성: Kafka로 전송
@app.post("/order")
async def create_order(order: OrderIn):
    await send_order_event(order.dict())
    return {"status": "Order event sent to Kafka"}

# 주문 목록 조회: DB에서 읽어오기
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/orders")
async def get_orders(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order))
    return result.scalars().all()
