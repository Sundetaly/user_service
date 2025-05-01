from logging.config import dictConfig

from fastapi import FastAPI

from app.configs.config import settings
from app.configs.log_config import LogConfig
from app.routes import router

dictConfig(LogConfig().dict())

app_configs = {"title": settings.APP_NAME}

if settings.ENVIRONMENT == "prod":
    app_configs["openapi_url"] = None

app = FastAPI(**app_configs)

app.include_router(router)
