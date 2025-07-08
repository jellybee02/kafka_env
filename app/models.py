from sqlalchemy import Column, Integer, String
from app.db import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    quantity = Column(Integer)
