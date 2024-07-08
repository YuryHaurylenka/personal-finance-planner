import uuid
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID,
)
from sqlalchemy import (
    ForeignKey,
    UUID,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from src.utils.types import UserIdType
from .base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTableUUID):
    user_id: Mapped[UserIdType] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
