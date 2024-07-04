from pydantic import BaseModel, ConfigDict


class BudgetBase(BaseModel):
    category: str
    limit_amount: float


class BudgetCreate(BudgetBase):
    pass


class Budget(BudgetBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    owner_id: int
