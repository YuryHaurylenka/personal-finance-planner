from fastapi_users import FastAPIUsers

from src.models import User
from src.utils.dependencies.auth import authentication_backend, get_user_manager
from src.utils.types import UserIdType

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)
