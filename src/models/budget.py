from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Budget(Base):
    __tablename__ = "budgets"

    budget_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False
    )
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Budget id={self.budget_id} amount={self.amount}>"
