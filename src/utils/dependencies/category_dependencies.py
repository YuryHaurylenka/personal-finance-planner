from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud import category as crud_category
from src.core import db_helper
from src.models import Category


async def category_by_id(
    category_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Category:
    category = await crud_category.get_category(
        session=session, category_id=category_id
    )
    if category is not None:
        return category

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category {category_id} not found!",
    )
