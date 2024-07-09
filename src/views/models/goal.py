from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.core.config import settings
from src.crud import goal as crud_goal
from src.schemas.goal import (
    Goal,
    GoalCreate,
    GoalUpdate,
    GoalUpdatePartial,
)
from src.utils.dependencies.models.goal_dependencies import goal_by_id

router = APIRouter(prefix=settings.api.v1.goals, tags=["Goals"])


@router.get("/", response_model=list[Goal])
async def get_goals(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_goal.get_goals(session=session)


@router.post(
    "/",
    response_model=Goal,
    status_code=status.HTTP_201_CREATED,
)
async def create_goal(
    goal_in: GoalCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_goal.create_goal(session=session, goal_in=goal_in)


@router.get("/{goal_id}/", response_model=Goal)
async def get_goal(
    goal: Goal = Depends(goal_by_id),
):
    return goal


@router.put("/{goal_id}/")
async def udpate_goal(
    goal_update: GoalUpdate,
    goal: Goal = Depends(goal_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_goal.update_goal(
        session=session,
        goal=goal,
        goal_update=goal_update,
    )


@router.patch("/{goal_id}/")
async def udpate_goal_partial(
    goal_update: GoalUpdatePartial,
    goal: Goal = Depends(goal_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_goal.update_goal(
        session=session,
        goal=goal,
        goal_update=goal_update,
        partial=True,
    )


@router.delete("/{goal_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_goal(
    goal: Goal = Depends(goal_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await crud_goal.delete_goal(session=session, goal=goal)
