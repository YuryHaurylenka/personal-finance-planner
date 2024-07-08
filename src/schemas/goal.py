import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator

from src.utils.dependencies.parse_timestamp import parse_timestamp


class GoalBase(BaseModel):
    amount: float
    description: str
    target_date: datetime

    @field_validator("target_date", mode="before")
    def validate_timestamp(cls, value):
        if isinstance(value, str):
            return parse_timestamp(value)
        return value


class GoalCreate(GoalBase):
    user_id: uuid.UUID
    category_id: Optional[int] = None


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
    category_id: Optional[int]
