from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, validates

from models import Base


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
