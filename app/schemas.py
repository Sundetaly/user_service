from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    telegram_id: str


class UserOut(UserCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
