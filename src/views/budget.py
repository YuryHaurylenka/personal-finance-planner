from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.crud import budget as crud_budget
from src.schemas.budget import (
    Budget,
    BudgetCreate,
    BudgetUpdate,
    BudgetUpdatePartial,
)
from src.utils.dependencies.budget_dependencies import budget_by_id

router = APIRouter(prefix="/budgets", tags=["Budgets"])


@router.get("/", response_model=list[Budget])
async def get_budgets(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_budget.get_budgets(session=session)


@router.post(
    "/",
    response_model=Budget,
    status_code=status.HTTP_201_CREATED,
)
async def create_budget(
    budget_in: BudgetCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_budget.create_budget(session=session, budget_in=budget_in)


@router.get("/{budget_id}/", response_model=Budget)
async def get_budget(
    budget: Budget = Depends(budget_by_id),
):
    return budget


@router.put("/{budget_id}/")
async def update_budget(
    budget_update: BudgetUpdate,
    budget: Budget = Depends(budget_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_budget.update_budget(
        session=session,
        budget=budget,
        budget_update=budget_update,
    )


@router.patch("/{budget_id}/")
async def update_budget_partial(
    budget_update: BudgetUpdatePartial,
    budget: Budget = Depends(budget_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_budget.update_budget(
        session=session,
        budget=budget,
        budget_update=budget_update,
        partial=True,
    )


@router.delete("/{budget_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_budget(
    budget: Budget = Depends(budget_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud_budget.delete_budget(session=session, budget=budget)
