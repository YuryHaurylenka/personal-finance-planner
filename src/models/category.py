import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.core.config import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), unique=True, nullable=False)

    transactions = relationship("Transaction", back_populates="category")
    budgets = relationship("Budget", back_populates="category")

    def __repr__(self):
        return f"<Category id={self.category_id} name={self.name}>"
