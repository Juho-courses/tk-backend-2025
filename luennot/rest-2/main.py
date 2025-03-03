from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

shoes = [
    {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
]


class ShoeBase(BaseModel):
    model: str
    manufacturer: str


class ShoeIn(ShoeBase):
    pass


class ShoeDb(ShoeBase):
    id: int


@app.post("/shoes", status_code=status.HTTP_201_CREATED)
def create_shoe(shoe_in: ShoeIn):
    new_id = len(shoes)
    shoe = ShoeDb(**shoe_in.model_dump(), id=new_id)
    shoes.append(shoe.model_dump())
    return shoe


@app.get("/shoes", response_model=list[ShoeDb])
def get_shoes(manufacturer: str = ""):
    if manufacturer != "":
        return [s for s in shoes if s["manufacturer"] == manufacturer]
    return shoes


@app.get("/shoes/{shoe_id}", response_model=ShoeDb)
def get_shoe_by_id(shoe_id: int):
    s = [s for s in shoes if s["id"] == shoe_id]
    if len(s) != 0:
        return s[0]
    else:
        raise HTTPException(
            detail=f"shoe {shoe_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )


@app.delete("/shoes/{shoe_id}")
def delete_shoe(shoe_id: int):
    s = [s for s in shoes if s["id"] == shoe_id]
    if len(s) != 0:
        del shoes[shoe_id]
        return {"message": f"Shoe {shoe_id} deleted."}
    else:
        raise HTTPException(
            detail=f"shoe {shoe_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
