import uuid

from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Budget, Goal, Transaction
from .user_transaction_association import user_transaction_association_table

from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="user"
    )
    goals: Mapped[list["Goal"]] = relationship("Goal", back_populates="user")
    budgets: Mapped[list["Budget"]] = relationship("Budget", back_populates="user")

    def __repr__(self):
        return f"<User name={self.username} email={self.email}>"
