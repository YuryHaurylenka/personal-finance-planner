import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from src.utils.hash_password import hash_password


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: bytes

    @field_validator("password")
    def hashing(cls, password) -> bytes:
        return hash_password(password)


class UserUpdate(UserBase):
    password: Optional[bytes]

    @field_validator("password")
    def hashing(cls, password: Optional[bytes]) -> Optional[bytes]:
        if password is not None:
            return hash_password(password)
        return password


class UserUpdatePartial(UserCreate):
    username: str | None = None
    email: str | None = None
    password: bytes | None = None
    is_active: bool | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    password: bytes
    # is_active: bool
