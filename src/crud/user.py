import uuid

from sqlalchemy import select
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from src.utils.hash_password import hash_password


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.user_id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: uuid.UUID) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    hashed_password = hash_password(user_in.password)
    db_user = User(
        username=user_in.username, email=user_in.email, hashed_password=hashed_password
    )
    session.add(db_user)
    await session.commit()
    return db_user


async def update_user(
    session: AsyncSession, user: User, user_in: UserUpdate, partial: bool = False
) -> User:
    if user_in.password:
        hashed_password = hash_password(user_in.password)
        setattr(user, "hashed_password", hashed_password)
    if user_in.username:
        setattr(user, "username", user_in.username)
    if user_in.email:
        setattr(user, "email", user_in.email)

    if partial:
        for attr, value in user_in.dict(exclude_unset=True, exclude_none=True).items():
            setattr(user, attr, value)

    await session.commit()
    return user


async def delete_user(session: AsyncSession, user: User) -> None:
    await session.delete(user)
    await session.commit()
