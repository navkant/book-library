from typing import List, Optional

from pydantic import BaseModel


class AuthorDomainModel(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class BookDomainModel(BaseModel):
    id: int
    title: str
    summary: str
    genre: str
    author: Optional[AuthorDomainModel]

    class Config:
        orm_mode = True


class BookListDomainModel(BaseModel):
    items: List[BookDomainModel]

    class Config:
        orm_mode = True
