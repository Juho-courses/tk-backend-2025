from fastapi import FastAPI
from .routers import shoes, manufacturers

app = FastAPI()

app.include_router(shoes.router)
app.include_router(manufacturers.router)
