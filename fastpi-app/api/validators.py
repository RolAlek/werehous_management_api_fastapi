from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import product_crud


async def check_exist(id: int, session: AsyncSession):
    db_obj = await product_crud.get_by_attribute("id", id, session)
    if db_obj is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Product with id {id} not found.",
        )
    return db_obj
