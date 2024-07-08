from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.crud import transaction as crud_transaction
from src.models import Transaction


async def transaction_by_id(
    transaction_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Transaction:
    transaction = await crud_transaction.get_transaction(
        session=session, transaction_id=transaction_id
    )
    if transaction is not None:
        return transaction

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Transaction {transaction_id} not found!",
    )
