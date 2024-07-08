from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .goal import Goal
    from .transaction import Transaction
    from .budget import Budget


class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="category"
    )
    goals: Mapped[list["Goal"]] = relationship("Goal", back_populates="category")
    budgets: Mapped[list["Budget"]] = relationship("Budget", back_populates="category")

    def __repr__(self):
        return f"<Category id={self.category_id} name={self.name}>"
