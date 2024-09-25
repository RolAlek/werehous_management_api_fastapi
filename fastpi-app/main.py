from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api import main_router
from core import db_manager
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start app
    yield
    # shutdown
    await db_manager.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(main_router, prefix=settings.api.api_prefix)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
