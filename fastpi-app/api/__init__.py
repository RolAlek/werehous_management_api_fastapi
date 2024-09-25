from fastapi import APIRouter

from api.endpoints.product import router as product_router
from core.config import settings

main_router = APIRouter()
main_router.include_router(
    product_router,
    prefix=settings.api.product_prefix,
    tags=["Products"],
)
