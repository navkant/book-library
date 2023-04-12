from typing import List, Optional

from pydantic import BaseModel


class AuthorDomainModel(BaseModel):
    first_name: str
    last_name: str


class BookResponse(BaseModel):
    id: int
    title: str
    summary: str
    genre: str
    author: Optional[AuthorDomainModel]

    class Config:
        orm_mode = True


class BookListResponse(BaseModel):
    items: List[BookResponse]

    class Config:
        orm_mode = True


class BookFilterRequest(BaseModel):
    genre: Optional[str]
    name: Optional[str]
