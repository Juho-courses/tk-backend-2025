from fastapi import APIRouter, status
from ..db.models import AuthorIn, AuthorOut
from ..db import author_crud

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/", response_model=list[AuthorOut])
def read_all_authors(name: str = ""):
    return author_crud.read_all_authors(name)


@router.get("/{author_id}", response_model=AuthorOut)
def read_author_by_id(author_id: int):
    return author_crud.read_author_by_id(author_id)


@router.post("/", response_model=AuthorOut, status_code=status.HTTP_201_CREATED)
def save_author(author_in: AuthorIn):
    return author_crud.save_author(author_in)


@router.delete("/{author_id}")
def delete_author_by_id(author_id: int):
    return author_crud.delete_author_by_id(author_id)
