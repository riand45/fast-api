import uuid
from typing import List
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy import text
import sqlalchemy.dialects.postgresql as pg

class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(sa_column=Column(pg.UUID, nullable=False, default=uuid.uuid4, primary_key=True))
    title: str = Field(sa_column=Column(String(100), nullable=False))
    author: str = Field(sa_column=Column(String(100), nullable=False))
    publisher: str = Field(sa_column=Column(String(100), nullable=False))
    published_date: datetime = Field(sa_column=Column(DateTime, nullable=False))
    page_count: int = Field(sa_column=Column(Integer, nullable=False))
    language: str = Field(sa_column=Column(String(50), nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime, nullable=False, server_default=text("now()")))
    updated_at: datetime = Field(sa_column=Column(DateTime, nullable=False, server_default=text("now()"), onupdate=datetime.now))
    user_uid: uuid.UUID = Field(sa_column=Column(pg.UUID, ForeignKey("users.uid"), nullable=True))
    user: "User" = Relationship(back_populates="books")

    def __repr__(self):
        return f"<Book {self.title}>"

class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    username: str
    email: str
    first_name: str
    last_name: str
    role: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False, server_default="user")
    )
    is_verified: bool = Field(default=False)
    password_hash: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False), exclude=True
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    books: List["Book"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )
    # reviews: List["Review"] = Relationship(
    #     back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    # )

    def __repr__(self):
        return f"<User {self.username}>"
    