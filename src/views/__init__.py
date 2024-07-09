from fastapi import APIRouter

from .auth import router as auth_router
from .models import router as models_router
from .fake_data import router as fake_data_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(models_router)
router.include_router(fake_data_router)
