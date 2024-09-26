from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    async def create(
        self,
        data_in: CreateSchemaType,
        session: AsyncSession,
    ) -> ModelType:
        new_data = data_in.model_dump()
        db_obj = self.model(**new_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get_multi(self, session: AsyncSession) -> list[ModelType]:
        objects = await session.scalars(select(self.model))
        return objects.all()

    async def get_by_attribute(
        self,
        attr_name: str,
        attr_value: str,
        session: AsyncSession,
    ) -> Optional[ModelType]:
        return await session.scalar(
            select(self.model)
            .where(getattr(self.model, attr_name) == attr_value)
        )


