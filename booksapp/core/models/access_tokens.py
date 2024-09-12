from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable
)

from .base import Base
from core.types.user_id import UserIdType


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    pass