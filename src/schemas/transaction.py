from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: float
    transaction_type: str
    category: str
    description: Optional[str] = None
    transaction_date: datetime


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
