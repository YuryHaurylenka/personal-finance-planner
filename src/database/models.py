import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declared_attr, relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<User name={self.username} email={self.email}>"


class Transaction(Base):
    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    description = Column(Text, nullable=True)

    user = relationship("User", back_populates="transactions")


class Goal(Base):
    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    goal_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    target_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="goals")


class Budget(Base):
    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    budget_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="budgets")
