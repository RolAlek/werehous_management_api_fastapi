from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_manager
from crud import order_crud
from schemas import CreateOrder, ReadOrder

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
