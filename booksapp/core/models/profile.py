from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .mixins import UserRelationMixin
from core.models import Base


class Profile(UserRelationMixin, Base):
    __tablename__ = 'profiles'
    _user_id_unique = True
    _user_back_populates = 'profile'

    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))