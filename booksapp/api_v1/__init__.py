from fastapi import APIRouter

from api_v1.auth.jwt_auth import router as jwt_router
from .auth_users import auth_router

router = APIRouter()
router.include_router(router=jwt_router)
router.include_router(router=auth_router)