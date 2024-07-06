from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.crud import goal as crud_goal
from src.models import Goal


async def goal_by_id(
    goal_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Goal:
    goal = await crud_goal.get_goal(session=session, goal_id=goal_id)
    if goal is not None:
        return goal

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Goal {goal_id} not found!",
    )
