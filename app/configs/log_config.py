from typing import Dict, Any, ClassVar
from pydantic import BaseModel

from app.configs.config import settings


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "user_service_log"
    LOG_FORMAT: str = "%(asctime)s %(levelname)s [] [%(thread)d] [] [%(name)s] %(message)s"
    LOG_LEVEL: str = "INFO" if settings.ENVIRONMENT == "prod" else "DEBUG"

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters: Dict[str, Dict[str, Any]] = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S,000",
        },
    }
    handlers: Dict[str, Dict[str, Any]] = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: Dict[str, Dict[str, Any]] = {
        "user_service_log": {"handlers": ["default"], "level": LOG_LEVEL},
        "uvicorn": {"handlers": ["default"], "level": LOG_LEVEL},
        "gunicorn": {"handlers": ["default"], "level": LOG_LEVEL},
    }