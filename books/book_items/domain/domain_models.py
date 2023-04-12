from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class BookItemDomainModel(BaseModel):
    id: int
    book_id: str
    book_item_id: str
    borrowed_by_id: Optional[int]
    borrowed_at: Optional[datetime]
    return_by: Optional[datetime]

    class Config:
        orm_mode = True


class BookItemsListDomainModel(BaseModel):
    items: List[BookItemDomainModel]
