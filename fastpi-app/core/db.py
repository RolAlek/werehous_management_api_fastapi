from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings


class DBManger:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_session(self):
        async with self.session_maker() as session:
            yield session


db_manager = DBManger(url=str(settings.db.url), echo=settings.db.echo)
