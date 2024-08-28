from sqlalchemy.orm import Mapped

from booksapp.core.models import Base


class Book(Base):
    __tablename__ = 'books'

    title: Mapped[str]


