from datetime import date

from pydantic import BaseModel

class GoalBase(BaseModel):
    description: str
    target_amount: float
    target_date: date

class GoalCreate(GoalBase):
    pass

class GoalInDb(GoalBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
