import uuid

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


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


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    description = Column(Text, nullable=True)

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction id={self.transaction_id} amount={self.amount}>"


class Goal(Base):
    __tablename__ = "goals"

    goal_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    target_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="goals")

    def __repr__(self):
        return f"<Goal id={self.goal_id} amount={self.amount}>"


class Budget(Base):
    __tablename__ = "budgets"

    budget_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="budgets")

    def __repr__(self):
        return f"<Budget id={self.budget_id} amount={self.amount}>"
