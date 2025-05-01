from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import User
from app.schemas import UserCreate


async def get_user_by_telegram(db: AsyncSession, telegram_id: str):
    result = await db.execute(select(User).where(User.telegram_id == telegram_id))
    return result.scalars().first()


async def create_user(db: AsyncSession, user_data: UserCreate):
    user = User(telegram_id=user_data.telegram_id)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
