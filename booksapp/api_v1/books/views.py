from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Book
from .dependencies import book_by_id
from . import crud
from core.models import db_helper
from .schemas import BookCreateSchema, BookSchema, BookUpdateSchema

router = APIRouter(tags=['Books'])

@router.get('/', response_model=list[BookSchema])
async def get_books(
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_books(session=session)


@router.post('/', response_model=BookSchema)
async def create_book(
    book_in: BookCreateSchema,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_book(session=session, book_in=book_in)


@router.get('/{book_id}', response_model=BookSchema)
async def get_book(
    book: Book = Depends(book_by_id)
):
    return book

@router.patch('/{book_id}', response_model=BookSchema)
async def update_book(
    book_in: BookUpdateSchema,
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_book(session=session, book=book, book_update=book_in)

@router.delete('{book_id}')
async def delete_book(
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.delete_book(session=session, book=book)
