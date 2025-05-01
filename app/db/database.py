from asyncio import current_task

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, async_scoped_session
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

from app.configs.config import settings

load_dotenv()


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.ECHO,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
)
SessionLocal = async_scoped_session(
    async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False),
    scopefunc=current_task,
)
Base = declarative_base()


async def get_db():
    async with SessionLocal() as session:
        yield session
