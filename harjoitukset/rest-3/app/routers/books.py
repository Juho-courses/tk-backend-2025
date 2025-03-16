from fastapi import APIRouter, status
from ..db.models import BookIn, BookOut
from ..db import books_crud

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookOut])
def read_all_books(author: str = ""):
    return books_crud.read_all_books(author)


@router.get("/{book_id}", response_model=BookOut)
def read_book_by_id(book_id: int):
    return books_crud.read_book_by_id(book_id)


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def save_book(book_in: BookIn):
    return books_crud.save_book(book_in)


@router.delete("/{book_id}")
def delete_book_by_id(book_id: int):
    return books_crud.delete_book_by_id(book_id)
