from fastapi import APIRouter

from src.views.user import router as users_router

router = APIRouter()
router.include_router(router=users_router, prefix="/users", tags=["Users"])
