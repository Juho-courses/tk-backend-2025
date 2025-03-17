from fastapi import FastAPI
from .routers import shoes, manufacturers
from contextlib import asynccontextmanager
from .db.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("startataan")
    # luo tietokanta
    create_db()
    yield
    print("lopetellaan")


app = FastAPI(lifespan=lifespan)

app.include_router(shoes.router)
app.include_router(manufacturers.router)
