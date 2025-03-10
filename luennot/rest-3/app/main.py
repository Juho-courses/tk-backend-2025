from fastapi import FastAPI
from .routers import shoes

app = FastAPI()

app.include_router(shoes.router)
