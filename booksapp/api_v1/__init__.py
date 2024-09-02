from fastapi import APIRouter

from api_v1.books.views import router as books_router
from api_v1.auth.jwt_auth import router as jwt_router

router = APIRouter()
router.include_router(router=books_router, prefix='/books')
router.include_router(router=jwt_router)