from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.core.config import settings
from src.crud import user as crud_user
from src.models.user import User
from src.schemas.user import UserCreate, UserRead, UserUpdate
from src.utils.dependencies.models.user_dependencies import user_by_id

router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])


@router.get("/", response_model=list[UserRead])
async def get_users(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_user.get_users(session=session)


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_user.create_user(session=session, user_in=user_in)


@router.get("/{user_id}/", response_model=UserRead)
async def get_user(
    user: User = Depends(user_by_id),
):
    return user


@router.put("/{user_id}/")
async def update_user(
    user_in: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_user.update_user(
        session=session,
        user=user,
        user_in=user_in,
    )


@router.patch("/{user_id}/")
async def update_user_partial(
    user_in: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_user.update_user(
        session=session,
        user=user,
        user_in=user_in,
        partial=True,
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await crud_user.delete_user(session=session, user=user)
