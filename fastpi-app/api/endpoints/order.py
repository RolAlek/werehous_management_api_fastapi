from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.validators import check_exists
from core import db_manager
from crud import order_crud
from models import Order
from schemas import CreateOrder, ReadOrder, UpdateOrder

router = APIRouter()


@router.post("/", response_model=ReadOrder)
async def create_order(
    new_order: CreateOrder,
    session: AsyncSession = Depends(db_manager.get_session),
):
    return await order_crud.create_order(new_order, session)


@router.get("/", response_model=list[ReadOrder])
async def get_all_orders(
    session: AsyncSession = Depends(db_manager.get_session),
):
    return await order_crud.get_all_orders(session)


@router.get("/{order_id}", response_model=ReadOrder)
async def get_order_by_id(
    order_id: int,
    session=Depends(db_manager.get_session),
):
    await check_exists(Order, order_id, session)
    return await order_crud.get_order(order_id, session)


@router.patch("/{order_id}/status", response_model=ReadOrder)
async def update_order_status(
    order_id: int,
    status: UpdateOrder,
    session=Depends(db_manager.get_session),
):
    await check_exists(Order, order_id, session)
    return await order_crud.update_order(order_id, status, session)
