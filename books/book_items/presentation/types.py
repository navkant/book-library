from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from books.book.presentation.types import BookResponse


class BookItemResponse(BaseModel):
    id: int
    book: BookResponse
    book_item_id: str
    borrowed_by_id: Optional[int]
    borrowed_at: Optional[datetime]
    return_by: Optional[datetime]

    class Config:
        orm_mode = True


class BookItemsListResponse(BaseModel):
    items: List[BookItemResponse]
