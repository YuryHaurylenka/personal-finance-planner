from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate

from src.utils.types import UserIdType


# change in BaseUser class id to user_id (in Model i have user_id)
class UserRead(BaseUser[UserIdType]):
    username: str


class UserCreate(BaseUserCreate):
    username: str


class UserUpdate(BaseUserUpdate):
    username: str
