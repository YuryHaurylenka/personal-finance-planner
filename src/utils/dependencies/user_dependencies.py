import uuid
from sqlalchemy.future import select
from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.crud import user as crud_user
from src.models import User


async def user_by_id(
    user_id: Annotated[uuid.UUID, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> User:
    user = await crud_user.get_user(session=session, user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found!",
    )


async def get_user_by_username(
    username: Annotated[str, Path],
    session: AsyncSession,
) -> User:
    result = await session.execute(select(User).filter(User.username == username))
    return result.scalars().one_or_none()
