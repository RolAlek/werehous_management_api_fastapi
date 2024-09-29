from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from models import OrderItem


class OrderStatus(Enum):
    PENDING = "Собирается"
    SHIPPED = "Доставляется"
    DELIVERED = "Доставлен"


class Order(Base):
    created_date: Mapped[datetime] = mapped_column(default=datetime.now)
    status: Mapped[OrderStatus] = mapped_column(
        SAEnum(
            OrderStatus,
            values_callable=lambda x: [e.value for e in x],
        ),
        default=OrderStatus.PENDING,
    )
    products_details: Mapped[list["OrderItem"]] = relationship(
        back_populates="order"
    )
