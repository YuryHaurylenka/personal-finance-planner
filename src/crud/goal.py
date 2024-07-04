from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.goal import Goal
from src.schemas.goal import (
    GoalCreate,
    GoalUpdate,
    GoalUpdatePartial,
)


async def get_goals(session: AsyncSession) -> list[Goal]:
    stmt = select(Goal).order_by(Goal.goal_id)
    result: Result = await session.execute(stmt)
    goals = result.scalars().all()
    return list(goals)


async def get_goal(session: AsyncSession, goal_id: int) -> Goal | None:
    return await session.get(Goal, goal_id)


async def create_goal(session: AsyncSession, goal_in: GoalCreate) -> Goal:
    goal = Goal(**goal_in.model_dump())
    session.add(goal)
    await session.commit()
    # await session.refresh(goal)
    return goal


async def update_goal(
    session: AsyncSession,
    goal: Goal,
    goal_update: GoalUpdate | GoalUpdatePartial,
    partial: bool = False,
) -> Goal:
    for name, value in goal_update.model_dump(exclude_unset=partial).items():
        setattr(goal, name, value)
    await session.commit()
    return goal


async def delete_goal(
    session: AsyncSession,
    goal: Goal,
) -> None:
    await session.delete(goal)
    await session.commit()
