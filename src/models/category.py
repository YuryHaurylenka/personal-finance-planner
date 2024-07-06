from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Goal, Transaction
from .base import Base


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

    def __repr__(self):
        return f"<Category id={self.category_id} name={self.name}>"
