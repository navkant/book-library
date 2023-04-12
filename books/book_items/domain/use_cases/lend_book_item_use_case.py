from dependency_injector.wiring import Provide
from pydantic import BaseModel

from books.book_items.data.book_item_abstract_repo import BookItemAbstractRepo
from books.book_items.domain.domain_models import BookItemDomainModel


class LendBookItemUseCase:
    def execute(
        self,
        book_item_lend_request: "BookItemLendRequest",
        book_item_repo: BookItemAbstractRepo = Provide[
            "book_item_container.book_item_repo"
        ],
    ) -> BookItemDomainModel:
        return book_item_repo.lend_book_item(
            book_item=BookItemDomainModel.from_orm(book_item_lend_request)
        )


class BookItemLendRequest(BaseModel):
    id: int
    book_id: int
    book_item_id: str
    borrowed_by_id: int
