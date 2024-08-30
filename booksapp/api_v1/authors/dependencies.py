from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper


async def author_by_id(
        author_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    author = ''