from fastapi import HTTPException
from ..db.models import AuthorIn, AuthorOut

authors = [
    {"id": 0, "name": "Author 1"},
    {"id": 1, "name": "Author 2"},
]


def read_all_authors(name: str = ""):
    if name == "":
        return authors
    return [b for b in authors if b["name"] == name]


def read_author_by_id(author_id: int):
    bs = [b for b in authors if b["id"] == author_id]
    if len(bs) == 0:
        raise HTTPException(
            status_code=404, detail=f"Author with id {author_id} not found"
        )

    return bs[0]


def save_author(author_in: AuthorIn):
    new_id = len(authors)
    author = AuthorOut(**author_in.model_dump(), id=new_id)
    authors.append(author.model_dump())
    return author


def delete_author_by_id(author_id: int):
    bs = [b for b in authors if b["id"] == author_id]
    if len(bs) == 0:
        raise HTTPException(
            status_code=404, detail=f"Author with id {author_id} not found"
        )
    del authors[author_id]
    return {"message": f"Author {author_id} deleted."}
