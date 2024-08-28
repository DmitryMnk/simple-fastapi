from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


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

db_helper = DB_ORM(settings.DATABASE_URL())
