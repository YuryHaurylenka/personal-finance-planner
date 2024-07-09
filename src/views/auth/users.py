from fastapi import APIRouter

from src.core.config import settings
from src.schemas.user import UserRead, UserUpdate
from src.utils.dependencies.auth.fastapi_users import fastapi_users

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users Auth"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
