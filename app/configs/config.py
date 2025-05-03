from functools import lru_cache
from typing import Optional, Dict, Any

from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "User service"

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int = 5432
    DB_SCHEMA: str = "public"

    DATABASE_URL: Optional[str] = None

    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10

    ECHO: bool = False

    ENVIRONMENT: str

    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> Any:
        env_values = info.data
        if isinstance(v, str):
            return v
        return (
            f"postgresql+asyncpg://"
            f"{env_values['DB_USER']}:{env_values['DB_PASSWORD']}@{env_values['DB_HOST']}/{env_values['DB_NAME']}"
        )

    class Config:
        env_file = ".env"
        extra = "allow"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
