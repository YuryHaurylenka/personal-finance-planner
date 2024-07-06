import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator

from src.utils.dependencies.parse_timestamp import parse_timestamp


class TransactionBase(BaseModel):
    amount: float
    timestamp: datetime
    description: Optional[str] = None

    @field_validator("timestamp", mode="before")
    def validate_timestamp(cls, value):
        if isinstance(value, str):
            return parse_timestamp(value)
        return value


class TransactionCreate(TransactionBase):
    user_id: uuid.UUID
    category_id: Optional[int] = None


class TransactionUpdate(TransactionBase):
    pass


class TransactionUpdatePartial(TransactionCreate):
    amount: float | None = None
    timestamp: datetime | None = None
    description: str | None = None
    category_id: int | None = None
    user_id: uuid.UUID | None = None


class Transaction(TransactionBase):
    model_config = ConfigDict(from_attributes=True)
    transaction_id: int
    user_id: uuid.UUID
    category_id: Optional[int]
