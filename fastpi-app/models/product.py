from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from models import OrderItem


class Product(Base):
    name: Mapped[str] = mapped_column(String(128), unique=True)
    description: Mapped[str]
    price: Mapped[float]
    in_stock: Mapped[int]
    orders_details: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )
