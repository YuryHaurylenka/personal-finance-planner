import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GoalBase(BaseModel):
    amount: float
    description: str
    target_date: datetime
    category_id: Optional[int] = None


class GoalCreate(GoalBase):
    user_id: uuid.UUID


class GoalUpdate(GoalBase):
    pass


class GoalUpdatePartial(GoalCreate):
    amount: float | None = None
    description: str | None = None
    target_date: datetime | None = None
    category_id: int | None = None
    user_id: uuid.UUID | None = None


class Goal(GoalBase):
    model_config = ConfigDict(from_attributes=True)
    goal_id: int
    user_id: uuid.UUID
