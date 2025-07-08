from pydantic import BaseModel

class OrderIn(BaseModel):
    item: str
    quantity: int