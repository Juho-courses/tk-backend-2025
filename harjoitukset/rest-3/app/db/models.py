from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    author: str


class BookIn(BaseBook):
    pass


class BookOut(BaseBook):
    id: int


class AuthorBase(BaseModel):
    name: str


class AuthorIn(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int
