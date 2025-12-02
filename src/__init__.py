from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Lifespan started")
    yield
    print(f"Lifespan ended")

version = "v1"

app = FastAPI(
    title="FastAPI CRUD",
    description="A REST API for CRUD operations using FastAPI",
    version=version,
    lifespan=life_span,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
