from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.crud import transaction as crud_transaction
from src.schemas.transaction import (
    Transaction,
    TransactionCreate,
    TransactionUpdate,
    TransactionUpdatePartial,
)
from src.utils.dependencies.transaction_dependencies import transaction_by_id

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/", response_model=list[Transaction])
async def get_transactions(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_transaction.get_transactions(session=session)


@router.post(
    "/",
    response_model=Transaction,
    status_code=status.HTTP_201_CREATED,
)
async def create_transaction(
    transaction_in: TransactionCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_transaction.create_transaction(
        session=session, transaction_in=transaction_in
    )


@router.get("/{transaction_id}/", response_model=Transaction)
async def get_transaction(
    transaction: Transaction = Depends(transaction_by_id),
):
    return transaction


@router.put("/{transaction_id}/")
async def update_transaction(
    transaction_update: TransactionUpdate,
    transaction: Transaction = Depends(transaction_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_transaction.update_transaciton(
        session=session,
        transaction=transaction,
        transaction_update=transaction_update,
    )


@router.patch("/{transaction_id}/")
async def update_transaction_partial(
    transaction_update: TransactionUpdatePartial,
    transaction: Transaction = Depends(transaction_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud_transaction.update_transaciton(
        session=session,
        transaction=transaction,
        transaction_update=transaction_update,
        partial=True,
    )


@router.delete("/{transaction_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(
    transaction: Transaction = Depends(transaction_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud_transaction.delete_transaction(session=session, transaction=transaction)
