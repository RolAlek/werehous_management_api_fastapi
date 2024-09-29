from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.validators import check_product
from models import Order, OrderItem
from schemas import CreateOrder, ReadOrder, ReadOrderItem

from .base import CRUDBase


class OrderCRUD(CRUDBase):
    @staticmethod
    async def create_order(
        order_in: CreateOrder,
        session: AsyncSession,
    ):
        new_order = Order()
        session.add(new_order)
        await session.commit()

        new_order_data = order_in.model_dump()

        products = []
        for product in new_order_data["products"]:
            product_in_stock = await check_product(
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

        new_order = await session.scalar(
            select(Order)
            .where(Order.id == new_order.id)
            .options(
                selectinload(Order.products_details)
                .joinedload(OrderItem.product)
            )
        )
        new_order.products_details = products
        order = ReadOrder(
            id=new_order.id,
            created_date=new_order.created_date,
            status=new_order.status,
            products_details=[
                ReadOrderItem(
                    id=item.product.id,
                    name=item.product.name,
                    price=item.product.price,
                    description=item.product.description,
                    count=item.count_in_cart,
                )
                for item in new_order.products_details
            ],
        )
        await session.commit()
        await session.refresh(new_order)
        return order

    @staticmethod
    async def get_all_orders(session: AsyncSession):
        orders = await session.scalars(
            select(Order).options(
                selectinload(Order.products_details).joinedload(OrderItem.product)
            )
        )
        return [
            ReadOrder(
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
            for order in orders
        ]

    @staticmethod
    async def get_order(order_id: int, session: AsyncSession):
        order = await session.scalar(
            select(Order)
            .where(Order.id == order_id)
            .options(
                selectinload(Order.products_details)
                .joinedload(OrderItem.product)
            ),
        )
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


crud_manager = OrderCRUD(Order)
