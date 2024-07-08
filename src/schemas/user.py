import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from src.utils.hash_password import hash_password


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def hashing(cls, password: str) -> str:
        return hash_password(password)


class UserUpdate(UserBase):
    password: Optional[str]

    @field_validator("password")
    def hashing(cls, password: Optional[str]) -> Optional[str]:
        if password is not None:
            return hash_password(password)
        return password


class UserUpdatePartial(UserCreate):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    is_verified: bool | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
