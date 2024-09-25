from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class OrderStatus(Enum):
    PENDING = "Собирается"
    SHIPPED = "Доставляется"
    DELIVERED = "Доставлен"


class OrderItem(Base):
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    amount: Mapped[int]


class Product(Base):
    name: Mapped[str] = mapped_column(String(128), unique=True)
    description: Mapped[str]
    price: Mapped[float]
    amount: Mapped[int]
    orders: Mapped[list["Order"]] = relationship(
        secondary="orderitem", back_populates="products"
    )


class Order(Base):
    created_date: Mapped[datetime] = mapped_column(default=datetime.now)
    status: Mapped[OrderStatus] = mapped_column(
        SAEnum(
            OrderStatus,
            values_callable=lambda x: [e.value for e in x],
        ),
        default=OrderStatus.PENDING,
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="orderitem",
        back_populates="orders",
    )
