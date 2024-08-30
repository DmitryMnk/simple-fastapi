from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from core.models import User


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    query = select(User).where(User.username == username)
    result: Result = await session.execute(query)
    user: User | None = result.scalar_one_or_none()
    return user

