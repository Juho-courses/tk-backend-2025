from fastapi import APIRouter, status
from ..db.models import ManufacturerDb, ManufacturerIn
from ..db import manufacturer_crud

router = APIRouter(prefix="/manufacturers", tags=["manufacturers"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_manufacturer(manu_in: ManufacturerIn):
    return manufacturer_crud.create_manu(manu_in)


@router.get("/", response_model=list[ManufacturerDb])
def get_manufacturers(manufacturer: str = ""):
    return manufacturer_crud.get_manufacturers(manufacturer)


@router.get("/{manu_id}", response_model=ManufacturerDb)
def get_manufacturer_by_id(manu_id: int):
    return manufacturer_crud.get_manufacturer_by_id(manu_id)


@router.delete("/{manu_id}")
def delete_manufacturer(manu_id: int):
    return manufacturer_crud.delete_manufacturer(manu_id)
