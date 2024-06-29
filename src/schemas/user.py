import uuid
from typing import Optional

from pydantic import EmailStr

from src.core.config import Base


class UserBase(Base):
    user_id: uuid.UUID
    username: str
    email: EmailStr
    is_active: bool


class UserCreate(UserBase):
    username: str
    email: EmailStr


class UserUpdate(UserBase):
    password: Optional[str]


class UserInDB(UserBase):
    user_id: uuid.UUID
    hashed_password: str

    class Config:
        orm_mode = True
