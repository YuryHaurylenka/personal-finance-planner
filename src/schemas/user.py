from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str]

class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True