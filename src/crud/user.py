from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import User
from src.schemas.user import UserCreate


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.user_id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> User | None:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user
