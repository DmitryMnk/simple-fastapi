from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str

class BookSchema(BookBase):

    model_config = ConfigDict(from_attributes=True)
    id: int


class BookCreateSchema(BookBase):
    pass

class BookUpdateSchema(BookCreateSchema):
    title: str | None = None