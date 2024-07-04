import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud import user as crud_user
from src.database import db_helper
from src.schemas.user import User, UserCreate, UserUpdate, UserUpdatePartial
from src.utils.dependencies.user_dependencies import user_by_id

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_user.get_users(session=session)


@router.post("/", response_model=User)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_user.create_user(session=session, user_in=user_in)


@router.get("/{user_id}/", response_model=User)
async def get_user(
    user_id: uuid.UUID,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await crud_user.get_user(user_id=user_id, session=session)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found!",
    )


@router.put("/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_user.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.patch("/{user_id}/")
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_user.update_user(
        session=session, user=user, user_update=user_update, partial=True
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud_user.delete_user(session=session, user=user)
