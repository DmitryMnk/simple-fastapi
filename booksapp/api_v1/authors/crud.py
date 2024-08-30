from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from core.models.book import Author


async def get_authors(session: AsyncSession) -> List[Author]:
    query = select(Author).order_by(Author.last_name)
    result: Result = await session.execute(query)
    authors: List[Author] = result.scalar().all()
    return authors


async def get_author(session: AsyncSession, author_id: int) -> Author | None:
    return await session.get(Author, author_id)

