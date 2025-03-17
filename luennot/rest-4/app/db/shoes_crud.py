from fastapi import HTTPException, status
from .models import ShoeDb, ShoeIn
from sqlmodel import Session, select


def create_shoe(session: Session, shoe_in: ShoeIn):
    s = ShoeDb.model_validate(shoe_in)
    session.add(s)
    session.commit()
    session.refresh(s)
    return s


def get_shoes(session: Session, manufacturer: str = ""):
    if manufacturer != "":
        return session.exec(
            select(ShoeDb).where(ShoeDb.manufacturer == manufacturer)
        ).all()
    return session.exec(select(ShoeDb)).all()


def get_shoe_by_id(session: Session, shoe_id: int):
    s = session.get(ShoeDb, shoe_id)
    if not s:
        raise HTTPException(
            detail=f"shoe {shoe_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
    return s


def delete_shoe(session: Session, shoe_id: int):
    s = session.get(ShoeDb, shoe_id)
    if not s:
        raise HTTPException(
            detail=f"shoe {shoe_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
    session.delete(s)
    session.commit()
    return {"message": f"shoe {shoe_id} deleted."}
