import secrets
from fastapi import Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from src.core import db_helper
from src.utils.dependencies import user_dependencies
from src.utils.hash_password import verify_password
from src.schemas.user import User
from .helpers import (
    TOKEN_TYPE_FIELD,
    ACCESS_TOKEN_TYPE,
    REFRESH_TOKEN_TYPE,
)
from . import jwt_utils as auth_utils

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="jwt/login/",
)


async def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:
    try:
        payload = auth_utils.decode_jwt(token=token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
        )
    return payload


def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"invalid token type {current_token_type!r} expected {token_type!r}",
    )


async def get_user_by_token_sub(payload: dict, session: AsyncSession) -> User:
    username: str | None = payload.get("sub")
    user = await user_dependencies.get_user_by_username(username, session)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_auth_user_from_token_of_type(token_type: str):
    async def get_auth_user_from_token(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> User:
        validate_token_type(payload, token_type)
        return await get_user_by_token_sub(payload, session)

    return get_auth_user_from_token


class UserGetterFromToken:
    def __init__(self, token_type: str):
        self.token_type = token_type

    async def __call__(
        self,
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> User:
        validate_token_type(payload, self.token_type)
        return await get_user_by_token_sub(payload, session)


get_current_auth_user = get_auth_user_from_token_of_type(ACCESS_TOKEN_TYPE)
get_current_auth_user_for_refresh = UserGetterFromToken(REFRESH_TOKEN_TYPE)


async def get_current_active_auth_user(
    user: User = Depends(get_current_auth_user),
):
    if user.is_active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="inactive user",
    )


async def validate_auth_user(
    username: str = Form(),
    password: bytes = Form(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    user = await user_dependencies.get_user_by_username(username, session)
    if user is None:
        raise unauthed_exc

    if not verify_password(password, user.password):
        print(f"Failed password verification for user {username}")
        raise unauthed_exc

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User inactive",
        )

    return user
