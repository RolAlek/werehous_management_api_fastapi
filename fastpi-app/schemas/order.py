from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OrderItem(BaseModel):
    product_id: int
    amount: int


class CreateOrder(BaseModel):
    products: list[OrderItem]


class ReadOrderItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    count: int


class ReadOrder(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_date: datetime
    products_details: list[ReadOrderItem]
    status: str
