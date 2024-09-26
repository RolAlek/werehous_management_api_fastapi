from pydantic import BaseModel, Field, field_validator


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=128)
    description: str | None = Field(None)
    price: float
    amount: int = 0

    @field_validator("price")
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0!")
        return round(value, 2)

    @field_validator('name')
    def validate_name(cls, value):
        if value is None:
            raise ValueError("Column `name` cant't be null.")
        return value


class ProductRead(ProductCreate):
    id: int
