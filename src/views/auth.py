from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import db_helper
from src.schemas.user import User
from src.utils.dependencies import user_dependencies
from src.utils.hash_password import verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])
security = HTTPBasic()


async def authenticate_user(
    username: str,
    password: str,
    session: AsyncSession,
) -> User:
    user = await user_dependencies.get_user_by_username(username, session)
    if user is None or not verify_password(password.encode("utf-8"), user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


async def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    return await authenticate_user(credentials.username, credentials.password, session)


@router.get("/basic-auth-username/")
async def demo_basic_auth_username(auth_user: User = Depends(get_current_user)):
    return {
        "message": f"Hi, {auth_user.username}!",
        "username": auth_user.username,
    }
