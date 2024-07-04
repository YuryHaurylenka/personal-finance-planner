import uuid

from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    budgets = relationship("Budget", back_populates="user")

    def __repr__(self):
        return f"<User name={self.username} email={self.email}>"
