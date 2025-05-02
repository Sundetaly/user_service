from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas import UserCreate, UserOut
from app import crud

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut, status_code=201)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing = await crud.get_user_by_telegram(db, user.telegram_id)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    return await crud.create_user(db, user)


@router.get("/", response_model=list[UserOut])
async def list_users(limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud.get_all_users(db, limit)
