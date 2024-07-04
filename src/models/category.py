from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.core.config import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    transactions = relationship("Transaction", back_populates="category")
    budgets = relationship("Budget", back_populates="category")

    def __repr__(self):
        return f"<Category id={self.category_id} name={self.name}>"
