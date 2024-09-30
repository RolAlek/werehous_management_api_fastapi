from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.validators import check_exists
from core import db_manager
from crud import product_crud
from models import Product
from schemas import ProductCreate, ProductRead, ProductUpdate

router = APIRouter()


@router.post("/", status_code=HTTPStatus.CREATED, response_model=ProductRead)
async def create_product(
    new_product: ProductCreate,
    session: AsyncSession = Depends(db_manager.get_session),
):
    return await product_crud.create(new_product, session)


@router.get("/", response_model=list[ProductRead])
async def get_products_multi(
    session: AsyncSession = Depends(db_manager.get_session),
):
    return await product_crud.get_multi(session)


@router.get("/{product_id}", response_model=ProductRead)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(db_manager.get_session),
):
    return await check_exists(Product, product_id, session)


@router.put("/{product_id}", response_model=ProductRead)
async def update_product(
    product_id: int,
    product_in: ProductUpdate,
    session: AsyncSession = Depends(
        db_manager.get_session,
    ),
):
    return await product_crud.update(
        product_in,
        await check_exists(Product, product_id, session),
        session,
    )


@router.delete("/{product_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(db_manager.get_session),
):
    await product_crud.remove(
        await check_exists(Product, product_id, session),
        session,
    )
