from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.validators import check_product_count
from models import Order, OrderItem
from schemas import CreateOrder, ReadOrder, ReadOrderItem, UpdateOrder

from .base import CRUDBase


class OrderCRUD(CRUDBase):

    async def _get_obj_order(
        self,
        session: AsyncSession,
        order_id: int | None = None,
    ) -> Order | list[Order]:
        stmt = select(self.model).options(
            selectinload(self.model.products_details)
            .joinedload(OrderItem.product)
        )

        if order_id is not None:
            stmt = stmt.where(self.model.id == order_id)
            return await session.scalar(stmt)

        return await session.scalars(stmt)

    @staticmethod
    def _prepare_answer(order: Order):
        return ReadOrder(
            id=order.id,
            created_date=order.created_date,
            status=order.status,
            products_details=[
                ReadOrderItem(
                    id=item.product.id,
                    name=item.product.name,
                    price=item.product.price,
                    description=item.product.description,
                    count=item.count_in_cart,
                )
                for item in order.products_details
            ],
        )

    async def create_order(
        self,
        order_in: CreateOrder,
        session: AsyncSession,
    ):
        new_order = Order()
        session.add(new_order)
        await session.commit()

        new_order_data = order_in.model_dump()

        products = []
        for product in new_order_data["products"]:
            product_in_stock = await check_product_count(
                product["product_id"],
                session,
                product["amount"],
            )
            products.append(
                OrderItem(
                    product=product_in_stock,
                    count_in_cart=product["amount"],
                ),
            )
            product_in_stock.in_stock -= product["amount"]

        new_order = await self._get_obj_order(session, new_order.id)
        new_order.products_details = products
        order = self._prepare_answer(new_order)
        await session.commit()
        await session.refresh(new_order)
        return order

    async def get_all_orders(self, session: AsyncSession) -> list[ReadOrder]:
        orders = await self._get_obj_order(session)
        return [self._prepare_answer(order) for order in orders]

    async def get_order(
        self,
        order_id: int,
        session: AsyncSession,
    ) -> ReadOrder:
        return self._prepare_answer(
            await self._get_obj_order(
                session,
                order_id,
            ),
        )

    async def update_order(
        self,
        order_id: int,
        status: UpdateOrder,
        session: AsyncSession,
    ):
        order = await self._get_obj_order(session, order_id)
        setattr(order, "status", status.status)
        response = self._prepare_answer(order)
        await session.commit()
        return response


crud_manager = OrderCRUD(Order)
