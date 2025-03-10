from fastapi import APIRouter, status
from ..db.models import ShoeIn, ShoeDb
from ..db import shoes_crud

router = APIRouter(prefix="/shoes", tags=["shoes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_shoe(shoe_in: ShoeIn):
    return shoes_crud.create_shoe(shoe_in)


@router.get("/", response_model=list[ShoeDb])
def get_shoes(manufacturer: str = ""):
    return shoes_crud.get_shoes(manufacturer)


@router.get("/{shoe_id}", response_model=ShoeDb)
def get_shoe_by_id(shoe_id: int):
    return shoes_crud.get_shoe_by_id(shoe_id)


@router.delete("/{shoe_id}")
def delete_shoe(shoe_id: int):
    return shoes_crud.delete_shoe(shoe_id)
