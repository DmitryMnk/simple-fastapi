from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy.orm import mapped_column

from core.models import Base




class User(Base):

    __tablename__ = 'users'

    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)


    def __str__(self):
        return f'{self.__class__.__name__}: {self.username!r}'

    def __repr__(self):
        return str(self)
