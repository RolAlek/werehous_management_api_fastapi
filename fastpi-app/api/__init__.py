from fastapi import APIRouter

from api.endpoints.order import router as order_router
from api.endpoints.product import router as product_router
from core.config import settings

main_router = APIRouter()
main_router.include_router(
    product_router,
    prefix=settings.api.product_prefix,
    tags=["Products"],
)
main_router.include_router(
    order_router,
    prefix=settings.api.order_prefix,
    tags=["Orders"],
)
