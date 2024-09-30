from http import HTTPStatus
from typing import TYPE_CHECKING, Type

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Product

if TYPE_CHECKING:
    from models import Base


async def check_exists(
    model: Type["Base"],
    obj_id: int,
    session: AsyncSession,
) -> Type["Base"]:
    obj = await session.scalar(select(model).where(model.id == obj_id))
    if obj is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"{model.__name__} with id `{obj_id}` not found.",
        )
    return obj


async def check_product_count(
    product_id: int,
    session: AsyncSession,
    amount: int | None = None,
) -> Product:
    product = await check_exists(Product, product_id, session)
    if (amount is not None) and (product.in_stock < amount):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                "Sorry bro... but your selected product isn't enough in stock"
            ),
        )
    return product
