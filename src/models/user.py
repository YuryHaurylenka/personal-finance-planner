import uuid
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
)
from sqlalchemy.dialects.postgresql import BYTEA, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from .base import Base

if TYPE_CHECKING:
    from .goal import Goal
    from .budget import Budget
    from .transaction import Transaction
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "users"

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(256), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        default=True, nullable=False, server_default="True"
    )

    transactions: Mapped["Transaction"] = relationship(back_populates="user")
    goals: Mapped[list["Goal"]] = relationship("Goal", back_populates="user")
    budgets: Mapped[list["Budget"]] = relationship("Budget", back_populates="user")

    def __repr__(self):
        return f"<User name={self.username} email={self.email}>"
