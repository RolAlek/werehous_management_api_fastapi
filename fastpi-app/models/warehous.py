from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, validates

from models import Base


class OrderStatus(Enum):
    PENDING = "Собирается"
    SHIPPED = "Доставляется"
    DELIVERED = "Доставлен"


class Product(Base):
    name: Mapped[str] = mapped_column(String(128), unique=True)
    description: Mapped[str]
    price: Mapped[float]
    amount: Mapped[int]

    @validates("price")
    def validate_price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0!")
        return round(value, 2)


class Order(Base):
    created_date: Mapped[datetime] = mapped_column(default=datetime.now)
    status: Mapped[OrderStatus] = mapped_column(
        SAEnum(
            OrderStatus,
            values_callable=lambda x: [e.value for e in x],
        ),
        default=OrderStatus.PENDING,
    )
