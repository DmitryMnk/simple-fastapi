from sqlalchemy.orm import Mapped

from core.models import Base


class Book(Base):
    __tablename__ = 'books'

    title: Mapped[str]

    def __str__(self):
        return f'{self.title}'
