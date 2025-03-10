from pydantic import BaseModel


class ManufacturerBase(BaseModel):
    name: str


class ManufacturerDb(ManufacturerBase):
    id: int


class ManufacturerIn(ManufacturerBase):
    pass


class ShoeBase(BaseModel):
    model: str
    manufacturer: str


class ShoeIn(ShoeBase):
    pass


class ShoeDb(ShoeBase):
    id: int
