from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session
from asyncio import current_task

from core.config import settings


class DB_ORM:

    def __init__(self, url):
        self.engine = create_async_engine(url=url)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()

db_helper = DB_ORM(settings.db_url)
