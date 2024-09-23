from pydantic_settings import BaseSettings
from pydantic import BaseModel, PostgresDsn


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class APIPrefix(BaseModel):
    prefix: str = "/api"


class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool = True


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()
    db: DBConfig


settings = Settings()
