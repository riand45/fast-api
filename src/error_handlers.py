from typing import Any
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from src.errors import (
    InvalidToken,
    RevokedToken,
    AccessTokenRequired,
    RefreshTokenRequired,
    UserAlreadyExists,
    InvalidCredentials,
    InsufficientPermission,
    BookNotFound,
    TagNotFound,
    TagAlreadyExists,
    UserNotFound
)


def register_all_errors(app: FastAPI):
    @app.exception_handler(InvalidToken)
    async def invalid_token_handler(request: Request, exc: InvalidToken):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Invalid or expired token", "detail": str(exc)}
        )

    @app.exception_handler(RevokedToken)
    async def revoked_token_handler(request: Request, exc: RevokedToken):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Token has been revoked", "detail": str(exc)}
        )

    @app.exception_handler(AccessTokenRequired)
    async def access_token_required_handler(request: Request, exc: AccessTokenRequired):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Access token required", "detail": str(exc)}
        )

    @app.exception_handler(RefreshTokenRequired)
    async def refresh_token_required_handler(request: Request, exc: RefreshTokenRequired):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Refresh token required", "detail": str(exc)}
        )

    @app.exception_handler(UserAlreadyExists)
    async def user_already_exists_handler(request: Request, exc: UserAlreadyExists):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"error": "User already exists", "detail": str(exc)}
        )

    @app.exception_handler(InvalidCredentials)
    async def invalid_credentials_handler(request: Request, exc: InvalidCredentials):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Invalid credentials", "detail": str(exc)}
        )

    @app.exception_handler(InsufficientPermission)
    async def insufficient_permission_handler(request: Request, exc: InsufficientPermission):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"error": "Insufficient permissions", "detail": str(exc)}
        )

    @app.exception_handler(BookNotFound)
    async def book_not_found_handler(request: Request, exc: BookNotFound):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Book not found", "detail": str(exc)}
        )

    @app.exception_handler(TagNotFound)
    async def tag_not_found_handler(request: Request, exc: TagNotFound):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Tag not found", "detail": str(exc)}
        )

    @app.exception_handler(TagAlreadyExists)
    async def tag_already_exists_handler(request: Request, exc: TagAlreadyExists):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"error": "Tag already exists", "detail": str(exc)}
        )

    @app.exception_handler(UserNotFound)
    async def user_not_found_handler(request: Request, exc: UserNotFound):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "User not found", "detail": str(exc)}
        )
