from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from src.core.db_helper import db_helper
from src.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield User.get_db(session=session)
