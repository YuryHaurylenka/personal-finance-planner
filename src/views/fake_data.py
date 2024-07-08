from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db_helper import db_helper
from src.utils.fake_data import create_fake_data

router = APIRouter(prefix="/create_fake_data", tags=["FakeData"])


@router.post("/create-fake-data/", status_code=status.HTTP_201_CREATED)
async def generate_fake_data(
    amount: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    if amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Number of entries must be greater than 0",
        )
    await create_fake_data(amount, session)
    return {"message": f"Successfully created {amount} fake entries"}
