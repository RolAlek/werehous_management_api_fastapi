from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Product


async def check_product(
    product_id: int,
    session: AsyncSession,
    amount: int | None = None,
) -> Product:
    product = await session.scalar(
        select(Product).where(Product.id == product_id)
    )
    if product is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Product with id {product_id} not found.",
        )
    if (amount is not None) and (product.in_stock < amount):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Sorry bro... but your selected product isn't enough"
                   " in stock",
        )
    return product
