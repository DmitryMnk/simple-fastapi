from typing import TYPE_CHECKING, List
from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import String
from sqlalchemy.testing.schema import mapped_column

from core.models import Base
if TYPE_CHECKING:
    from .profile import Profile
    from .book import Book

class User(Base, SQLAlchemyBaseUserTable[int]):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(40))
    profile: Mapped['Profile'] = relationship(back_populates='user')
    books: Mapped[List['Book']] = relationship(back_populates='users', secondary='user_books')


    def __str__(self):
        return f'{self.__class__.__name__}: {self.username!r}'

    def __repr__(self):
        return str(self)
