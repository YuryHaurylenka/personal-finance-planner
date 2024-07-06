from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

from .base import Base

user_transaction_association_table = Table(
    "user_transaction_association",
    Base.metadata,
    Column("user_transaction_id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.user_id"), nullable=False),
    Column("transaction_id", ForeignKey("transactions.transaction_id"), nullable=False),
    UniqueConstraint(
        "user_id", "transaction_id", name="idx_unique_user_transaction_association"
    ),
)
