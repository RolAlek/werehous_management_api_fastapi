from datetime import datetime

from pydantic import BaseModel, ConfigDict

from models.order import OrderStatus


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


class UpdateOrder(BaseModel):
    status: OrderStatus


class ReadOrder(UpdateOrder):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_date: datetime
    products_details: list[ReadOrderItem]
