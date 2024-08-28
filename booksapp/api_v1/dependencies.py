from fastapi import Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1 import crud
from books.models import Book
from core.models import db_helper


async def book_by_id(
    book_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Book:
    book = await crud.get_book(session=session, book_id=book_id)
    if book is not None:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Книга с id = {book_id} не найдена'
    )