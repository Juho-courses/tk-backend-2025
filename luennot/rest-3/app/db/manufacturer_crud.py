from fastapi import HTTPException, status
from .models import ManufacturerIn, ManufacturerDb

manus = [
    {"id": 0, "name": "Hoka"},
    {"id": 1, "name": "Nike"},
]


def create_manu(manu_in: ManufacturerIn):
    new_id = len(manus)
    m = ManufacturerDb(**manu_in.model_dump(), id=new_id)
    manus.append(m.model_dump())
    return m


def get_manufacturers(manufacturer: str = ""):
    if manufacturer != "":
        return [s for s in manus if s["name"] == manufacturer]
    return manus


def get_manufacturer_by_id(manu_id: int):
    s = [s for s in manus if s["id"] == manu_id]
    if len(s) != 0:
        return s[0]
    else:
        raise HTTPException(
            detail=f"manufacturer {manu_id} not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )


def delete_manufacturer(manu_id: int):
    s = [s for s in manus if s["id"] == manu_id]
    if len(s) != 0:
        del manus[manu_id]
        return {"message": f"Shoe {manu_id} deleted."}
    else:
        raise HTTPException(
            detail=f"manufacturer {manu_id} not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
