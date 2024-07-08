from fastapi import APIRouter, Depends

from src.auth.helpers import get_current_user
from src.schemas.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/basic-auth-username/")
async def basic_auth_username(auth_user: User = Depends(get_current_user)):
    return {
        "message": f"Hi, {auth_user.username}!",
        "username": auth_user.username,
    }
