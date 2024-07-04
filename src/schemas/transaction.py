from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TransactionBase(BaseModel):
    amount: float
    transaction_type: str
    category: str
    description: Optional[str] = None
    transaction_date: datetime


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    owner_id: int

    class Config:
        orm_mode = True
