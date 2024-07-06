__all__ = (
    "budget_router",
    "category_router",
    "transaction_router",
    "fake_data_router",
    "goal_router",
    "user_router",
)

from .budget import router as budget_router
from .category import router as category_router
from .fake_data import router as fake_data_router
from .goal import router as goal_router
from .transaction import router as transaction_router
from .user import router as user_router
