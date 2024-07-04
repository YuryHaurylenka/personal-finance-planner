import uuid

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.transaction import Transaction
from src.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionUpdatePartial,
)


async def get_transactions(session: AsyncSession) -> list[Transaction]:
    stmt = select(Transaction).order_by(Transaction.transaction_id)
    result: Result = await session.execute(stmt)
    transactions = result.scalars().all()
    return list(transactions)


async def get_transaction(
    session: AsyncSession, transaction_id: int
) -> Transaction | None:
    return await session.get(Transaction, transaction_id)


async def create_transaction(
    session: AsyncSession, transaction_in: TransactionCreate
) -> Transaction:
    transaction = Transaction(**transaction_in.model_dump())
    session.add(transaction)
    await session.commit()
    # await session.refresh(transaction)
    return transaction


async def update_transaciton(
    session: AsyncSession,
    transaction: Transaction,
    transaction_update: TransactionUpdate | TransactionUpdatePartial,
    partial: bool = False,
) -> Transaction:
    for name, value in transaction_update.model_dump(exclude_unset=partial).items():
        setattr(transaction, name, value)
    await session.commit()
    return transaction


async def delete_transaction(
    session: AsyncSession,
    transaction: Transaction,
) -> None:
    await session.delete(transaction)
    await session.commit()
