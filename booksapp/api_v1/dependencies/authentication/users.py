from typing import TYPE_CHECKING, Annotated

from fastapi.params import Depends


from core.models import db_helper, User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



async def get_user_db(session: Annotated["AsyncSession", Depends(db_helper.session_dependency)]):
    yield User.get_db(session=session)