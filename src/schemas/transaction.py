from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional
import uuid


class TransactionBase(BaseModel):
    amount: float
    timestamp: datetime
    description: Optional[str] = None
    category_id: Optional[int] = None


class TransactionCreate(TransactionBase):
    user_id: uuid.UUID


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
