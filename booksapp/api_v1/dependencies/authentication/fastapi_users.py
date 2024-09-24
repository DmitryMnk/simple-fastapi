from fastapi_users import FastAPIUsers

from core.authentication.depebdencies import get_user_manager
from core.models import User
from core.types.user_id import UserIdType
from .backend import auth_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [auth_backend]
)