from fastapi import APIRouter

from api_v1.dependencies.authentication.backend import auth_backend
from api_v1.dependencies.authentication.fastapi_users import fastapi_users
from core.schemas.user import UserRead, UserCreate

auth_router = APIRouter(
    prefix='/auth/jwt',
    tags=['Auth']
)

auth_router.include_router(
    router=fastapi_users.get_auth_router(auth_backend),
)

auth_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)