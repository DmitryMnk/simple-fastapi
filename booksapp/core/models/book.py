import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from core.models import Base


class Book(Base):
    __tablename__ = 'books'

    title: Mapped[str]

    def __str__(self):
        return f'{self.title}'


class Author(Base):
    __tablename__ = 'authors'

    first_name: Mapped[str]
    second_name: Mapped[str | None]
    last_name: Mapped[str]
    date_of_birth: Mapped[datetime.datetime]