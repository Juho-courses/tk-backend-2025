from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class BaseBook(BaseModel):
    title: str
    author: str


class BookIn(BaseBook):
    pass


class BookOut(BaseBook):
    id: int


books = [
    {"id": 0, "title": "Book 1", "author": "Author 1"},
    {"id": 1, "title": "Book 2", "author": "Author 2"},
    {"id": 2, "title": "Book 3", "author": "Author 1"},
]


@app.get("/books", response_model=list[BookOut])
def read_all_books(author: str = ""):
    if author == "":
        return books
    return [b for b in books if b["author"] == author]


@app.get("/books/{book_id}", response_model=BookOut)
def read_book_by_id(book_id: int):
    bs = [b for b in books if b["id"] == book_id]
    if len(bs) == 0:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

    return bs[0]


@app.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def save_book(book_in: BookIn):
    new_id = len(books)
    book = BookOut(**book_in.model_dump(), id=new_id)
    books.append(book.model_dump())
    return book


@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int):
    bs = [b for b in books if b["id"] == book_id]
    if len(bs) == 0:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    del books[book_id]
    return {"message": f"Book {book_id} deleted."}
