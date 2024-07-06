import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator

from src.utils.dependencies.parse_timestamp import parse_timestamp


class BudgetBase(BaseModel):
    amount: float
    start_date: datetime
    end_date: datetime

    @field_validator("start_date", mode="before")
    def validate_timestamp(cls, value):
        if isinstance(value, str):
            return parse_timestamp(value)
        return value

    @field_validator("end_date", mode="before")
    def validate_timestamp(cls, value):
        if isinstance(value, str):
            return parse_timestamp(value)
        return value


class BudgetCreate(BudgetBase):
    user_id: uuid.UUID
    category_id: int


class BudgetUpdate(BudgetBase):
    pass


class BudgetUpdatePartial(BudgetCreate):
    amount: float | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    user_id: uuid.UUID | None = None
    category_id: int | None = None


class Budget(BudgetBase):
    model_config = ConfigDict(from_attributes=True)
    budget_id: int
    user_id: uuid.UUID
    category_id: int
