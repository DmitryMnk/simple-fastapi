import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from .mixins import UserRelationMixin
from core.models import Base
if TYPE_CHECKING:
    from .user import User

class Book(Base):
    __tablename__ = 'books'

    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(
        ForeignKey('authors.id')
    )
    author: Mapped["Author"] = relationship(back_populates='books')
    users: Mapped[List['User']] = relationship(back_populates='books', secondary='user_books')

    def __str__(self):
        return f'{self.title}'


class Author(Base):
    __tablename__ = 'authors'

    first_name: Mapped[str] = mapped_column(String(40))
    second_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    date_of_birth: Mapped[datetime.datetime]

    books: Mapped[List['Book']] = relationship(back_populates='author')


class UserBook(Base):
    __tablename__ = "user_books"
    __table_args__ = (
        UniqueConstraint(
            'user_id',
            'book_id',
            name='idx_unique_book_user'
        ),
    )

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
