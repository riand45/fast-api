import uuid
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, DateTime
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

    def __repr__(self):
        return f"<Book {self.title}>"
    