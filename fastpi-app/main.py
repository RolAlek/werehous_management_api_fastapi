import uvicorn
from fastapi import FastAPI

from api import main_router
from core.config import settings

main_app = FastAPI()
main_app.include_router(main_router, prefix=settings.api.prefix)

if __name__ == '__main__':
    uvicorn.run('main:main_app', reload=True)
