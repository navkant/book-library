from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from books.book.domain.domain_models import BookDomainModel


class BookItemDomainModel(BaseModel):
    id: int
    book: BookDomainModel
    book_item_id: str
    borrowed_by_id: Optional[int]
    borrowed_at: Optional[datetime]
    return_by: Optional[datetime]

    class Config:
        orm_mode = True


class BookItemsListDomainModel(BaseModel):
    items: List[BookItemDomainModel]
