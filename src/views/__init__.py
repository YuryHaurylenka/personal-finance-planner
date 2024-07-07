from fastapi import APIRouter

from .budget import router as budget_router
from .category import router as category_router
from .fake_data import router as fake_data_router
from .goal import router as goal_router
from .transaction import router as transaction_router
from .user import router as user_router
from .demo_auth import router as demo_auth_router

router = APIRouter()
router.include_router(budget_router)
router.include_router(category_router)
router.include_router(fake_data_router)
router.include_router(goal_router)
router.include_router(transaction_router)
router.include_router(user_router)
router.include_router(demo_auth_router)
