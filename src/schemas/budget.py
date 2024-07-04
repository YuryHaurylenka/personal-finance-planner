import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BudgetBase(BaseModel):
    amount: float
    category: str
    start_date: datetime
    end_date: datetime


class BudgetCreate(BudgetBase):
    user_id: uuid.UUID


class BudgetUpdate(BudgetBase):
    pass


class BudgetUpdatePartial(BudgetCreate):
    amount: float | None = None
    category: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    user_id: uuid.UUID | None = None


class Budget(BudgetBase):
    model_config = ConfigDict(from_attributes=True)
    budget_id: int
    user_id: uuid.UUID
