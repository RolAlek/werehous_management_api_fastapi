from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class APIPrefix(BaseModel):
    prefix: str = "/api"


class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool = True


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
        extra="allow",
    )
    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()
    db: DBConfig


settings = Settings()
