from pydantic import BaseModel


class ShoeBase(BaseModel):
    model: str
    manufacturer: str


class ShoeIn(ShoeBase):
    pass


class ShoeDb(ShoeBase):
    id: int
