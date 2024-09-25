from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base


ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, data_in: CreateSchemaType, session: AsyncSession):
        new_data = data_in.model_dump()
        db_obj = self.model(**new_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
