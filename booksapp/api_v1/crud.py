from typing import List
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Book
from .schemas import BookCreateSchema, BookUpdateSchema


async def get_books(session: AsyncSession) -> List[Book]:
    query = select(Book).order_by(Book.title)
    result: Result = await session.execute(query)
    books = result.scalars().all()
    return list(books)


async def get_book(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)


async def create_book(session: AsyncSession, book_in: BookCreateSchema) -> Book:
    book = Book(**book_in.model_dump())
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book


async def update_book(
    session: AsyncSession,
    book: Book,
    book_update: BookUpdateSchema) -> Book:

    for name, value in book_update.model_dump(exclude_unset=True).items():
        setattr(book, name, value)
    await session.commit()
    return book

async def delete_book(
    session: AsyncSession,
    book: Book,
) -> None:
    await session.delete(book)
    await session.commit()