from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import String
from sqlalchemy.testing.schema import mapped_column

from core.models import Base
if TYPE_CHECKING:
    from .profile import Profile


class User(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(40))

    profile: Mapped['Profile'] = relationship(back_populates='user')

