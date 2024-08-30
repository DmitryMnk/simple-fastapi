from typing import List

from pydantic import BaseModel, ConfigDict

from core.models import Author, User


class BookBase(BaseModel):
    title: str
    author: Author
    users: List[User]

class BookSchema(BookBase):

    model_config = ConfigDict(from_attributes=True)
    id: int


class BookCreateSchema(BookBase):
    pass

class BookUpdateSchema(BookCreateSchema):
    title: str | None = None