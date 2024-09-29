from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Product(Base):
    name: Mapped[str] = mapped_column(String(128), unique=True)
    description: Mapped[str]
    price: Mapped[float]
    in_stock: Mapped[int]
