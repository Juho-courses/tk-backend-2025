from sqlmodel import SQLModel, Field


class ManufacturerBase(SQLModel):
    name: str


class ManufacturerDb(ManufacturerBase):
    id: int


class ManufacturerIn(ManufacturerBase):
    pass


class ShoeBase(SQLModel):
    model: str
    manufacturer: str


class ShoeIn(ShoeBase):
    pass


class ShoeDb(ShoeBase, table=True):
    id: int = Field(default=None, primary_key=True)
