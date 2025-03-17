from fastapi import APIRouter, status, Depends
from ..db.models import ShoeIn, ShoeDb
from ..db import shoes_crud
from ..db.database import get_session
from sqlmodel import Session


router = APIRouter(prefix="/shoes", tags=["shoes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_shoe(shoe_in: ShoeIn, session: Session = Depends(get_session)):
    return shoes_crud.create_shoe(session, shoe_in)


@router.get("/", response_model=list[ShoeDb])
def get_shoes(manufacturer: str = "", session: Session = Depends(get_session)):
    return shoes_crud.get_shoes(session, manufacturer)


@router.get("/{shoe_id}", response_model=ShoeDb)
def get_shoe_by_id(shoe_id: int, session: Session = Depends(get_session)):
    return shoes_crud.get_shoe_by_id(session, shoe_id)


@router.delete("/{shoe_id}")
def delete_shoe(shoe_id: int, session: Session = Depends(get_session)):
    return shoes_crud.delete_shoe(session, shoe_id)
