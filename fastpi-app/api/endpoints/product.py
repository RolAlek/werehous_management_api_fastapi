from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ProductRead, ProductCreate
from core import db_manager
from crud import product_crud


router = APIRouter()


@router.post("/", status_code=HTTPStatus.CREATED, response_model=ProductRead)
async def create_product(
    new_product: ProductCreate,
    session: AsyncSession = Depends(db_manager.get_session),
):
    return await product_crud.create(new_product, session)
