import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    user_id: uuid.UUID
    username: str
    email: EmailStr
    is_active: bool


class UserCreate(UserBase):
    username: str
    email: EmailStr


class UserUpdate(UserBase):
    password: Optional[str]


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: uuid.UUID
    hashed_password: str
