from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.crud import budget as crud_budget
from src.models import Budget


async def budget_by_id(
    budget_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Budget:
    budget = await crud_budget.get_budget(session=session, budget_id=budget_id)
    if budget is not None:
        return budget

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category {budget_id} not found!",
    )
