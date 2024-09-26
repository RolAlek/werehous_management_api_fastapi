from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
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


@router.get("/", response_model=list[ProductRead])
async def get_products_multi(session: AsyncSession = Depends(db_manager.get_session)):
    return await product_crud.get_multi(session)


@router.get("/{product_id}", response_model=ProductRead)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(db_manager.get_session),
):
    product = await product_crud.get_by_attribute("id", product_id, session)
    if product is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Product with {product_id} not found.",
        )
    return product
