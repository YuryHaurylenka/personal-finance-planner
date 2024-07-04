from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.budget import Budget
from src.schemas.budget import (
    BudgetCreate,
    BudgetUpdate,
    BudgetUpdatePartial,
)


async def get_budgets(session: AsyncSession) -> list[Budget]:
    stmt = select(Budget).order_by(Budget.budget_id)
    result: Result = await session.execute(stmt)
    budgets = result.scalars().all()
    return list(budgets)


async def get_budget(session: AsyncSession, budget_id: int) -> Budget | None:
    return await session.get(Budget, budget_id)


async def create_budget(session: AsyncSession, category_in: BudgetCreate) -> Budget:
    budget = Budget(**category_in.model_dump())
    session.add(budget)
    await session.commit()
    # await session.refresh(category)
    return budget


async def update_budget(
    session: AsyncSession,
    budget: Budget,
    budget_update: BudgetUpdate | BudgetUpdatePartial,
    partial: bool = False,
) -> Budget:
    for name, value in budget_update.model_dump(exclude_unset=partial).items():
        setattr(budget, name, value)
    await session.commit()
    return budget


async def delete_budget(
    session: AsyncSession,
    budget: Budget,
) -> None:
    await session.delete(budget)
    await session.commit()
