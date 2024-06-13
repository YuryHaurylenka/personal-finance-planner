from pydantic import BaseModel


class BudgetBase(BaseModel):
    category: str
    limit_amount: float


class BudgetCreate(BudgetBase):
    pass

class BudgetInDB(BudgetBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True