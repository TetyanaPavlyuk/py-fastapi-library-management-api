from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class AuthorList(AuthorBase):
    id: int
    books: List[BookList]

    class Config:
        orm_mode = True


class AuthorDetail(AuthorBase):
    id: int = Field(..., gt=0)
    books: List[BookDetail]

    class Config:
        orm_mode = True


class AuthorUpdate(AuthorBase):
    id: int = Field(..., gt=0)
    name: Optional[str] = None
    bio: Optional[str] = None

    class Config:
        orm_mode = True


class AuthorDelete(BaseModel):
    id: int = Field(..., gt=0)

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: str


class BookCreate(BookBase):
    author_id: int = Field(..., gt=0)


class BookList(BookBase):
    id: int
    author: AuthorDetail

    class Config:
        orm_mode = True


class BookDetail(BookBase):
    id: int = Field(..., gt=0)
    author: AuthorDetail

    class Config:
        orm_mode = True


class BookUpdate(BookBase):
    id: int = Field(..., gt=0)
    title: Optional[str] = None
    summary: Optional[str] = None
    publication_date: Optional[str] = None
    author_id: Optional[int] = None

    class Config:
        orm_mode = True


class BookDelete(BaseModel):
    id: int = Field(..., gt=0)

    class Config:
        orm_mode = True
