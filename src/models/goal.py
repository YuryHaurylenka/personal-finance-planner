from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.core.config import Base


class Goal(Base):
    __tablename__ = "goals"

    goal_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)
    amount = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    target_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="goals")
    category = relationship("Category", back_populates="transactions")

    def __repr__(self):
        return f"<Goal id={self.goal_id} amount={self.amount}>"
