from fastapi import APIRouter, status, Depends
from src.books.schema import Book, BookCreateModel, BookUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.db.main import get_session
from typing import List
from src.auth.dependencies import AccessTokenBearer

book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_model=List[Book])
async def get_all_books(
    session: AsyncSession = Depends(get_session), 
    _:dict = Depends(AccessTokenBearer)
):
    return await book_service.get_all_books(session)

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(
    book_data: BookCreateModel, 
    session: AsyncSession = Depends(get_session), 
    _:dict = Depends(AccessTokenBearer)
):
    return await book_service.create_book(book_data, session)

@book_router.get("/{book_id}", response_model=Book)
async def get_book(
    book_id: str, 
    session: AsyncSession = Depends(get_session), 
    _:dict = Depends(AccessTokenBearer)
):
    return await book_service.get_book(book_id, session)

@book_router.patch("/{book_id}", response_model=Book)
async def update_book(
    book_id: str, 
    book_update_data: BookUpdateModel, 
    session: AsyncSession = Depends(get_session), 
    _:dict = Depends(AccessTokenBearer)
):
    return await book_service.update_book(book_id, book_update_data, session)

@book_router.delete("/{book_id}", response_model=Book)
async def delete_book(
    book_id: str, 
    session: AsyncSession = Depends(get_session), 
    _:dict = Depends(AccessTokenBearer)
):
    return await book_service.delete_book(book_id, session)
