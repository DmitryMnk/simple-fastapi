from fastapi import APIRouter

from api_v1.books.views import router as books_router

router = APIRouter()
router.include_router(router=books_router, prefix='/books')
