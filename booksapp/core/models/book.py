import datetime
from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from core.models import Base


class Book(Base):
    __tablename__ = 'books'

    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(
        ForeignKey('authors.id')
    )
    author: Mapped["Book"] = relationship(back_populates='books')

    def __str__(self):
        return f'{self.title}'


class Author(Base):
    __tablename__ = 'authors'

    first_name: Mapped[str] = mapped_column(String(40))
    second_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    date_of_birth: Mapped[datetime.datetime]

    books: Mapped[List['Book']] = relationship(back_populates='author')