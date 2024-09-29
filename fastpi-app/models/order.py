from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


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
