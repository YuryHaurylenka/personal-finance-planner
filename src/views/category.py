from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.crud import category as crud_category
from src.schemas.category import (
    Category,
    CategoryCreate,
    CategoryUpdate,
    CategoryUpdatePartial,
)
from src.utils.dependencies.category_dependencies import category_by_id

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[Category])
async def get_categories(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_category.get_categories(session=session)


@router.post(
    "/",
    response_model=Category,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    category_in: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_category.create_category(session=session, category_in=category_in)


@router.get("/{category_id}/", response_model=Category)
async def get_category(
    category: Category = Depends(category_by_id),
):
    return category


@router.put("/{category_id}/")
async def update_category(
    category_update: CategoryUpdate,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_category.update_category(
        session=session,
        category=category,
        category_update=category_update,
    )


@router.patch("/{category_id}/")
async def update_category_partial(
    category_update: CategoryUpdatePartial,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud_category.update_category(
        session=session,
        category=category,
        category_update=category_update,
        partial=True,
    )


@router.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await crud_category.delete_category(session=session, category=category)
