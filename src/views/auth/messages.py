from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from src.core.config import settings
from src.models import User
from src.schemas.user import UserRead
from src.utils.dependencies.auth.fastapi_users import (
    current_active_superuser,
    current_active_user,
)

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("")
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_active_user),
    ],
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(current_active_superuser),
    ],
):
    return {
        "messages": ["secret-m1", "secret-m2", "secret-m3"],
        "user": UserRead.model_validate(user),
    }
