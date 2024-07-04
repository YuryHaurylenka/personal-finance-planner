from datetime import date

from pydantic import BaseModel, ConfigDict


class GoalBase(BaseModel):
    description: str
    target_amount: float
    target_date: date


class GoalCreate(GoalBase):
    pass


class GoalI(GoalBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    owner_id: int
