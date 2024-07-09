from fastapi import APIRouter

from src.views.models.budget import router as budget_router
from src.views.models.category import router as category_router
from src.views.models.goal import router as goal_router
from src.views.models.transaction import router as transaction_router
from src.views.models.user import router as user_router

router = APIRouter()
router.include_router(user_router)
router.include_router(category_router)
router.include_router(transaction_router)
router.include_router(goal_router)
router.include_router(budget_router)
