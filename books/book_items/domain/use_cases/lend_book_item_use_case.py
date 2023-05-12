from dependency_injector.wiring import Provide
from pydantic import BaseModel

from books.book_items.data.book_item_abstract_repo import BookItemAbstractRepo
from books.book_items.domain.domain_models import BookItemDomainModel
from books.book_items.exceptions import BookItemAlreadyLent


class LendBookItemUseCase:
    def execute(
        self,
        book_item_lend_request: "BookItemLendRequest",
        book_item_repo: BookItemAbstractRepo = Provide[
            "book_item_container.book_item_repo"
        ],
    ) -> BookItemDomainModel:
        if book_item_repo.check_borrowed_book_item(
            book_item_id=book_item_lend_request.id,
            borrowed_by_id=book_item_lend_request.borrowed_by_id,
        ):
            raise BookItemAlreadyLent(
                f"Book Item {book_item_lend_request.id}, {book_item_lend_request.book_item_id} already lent to user {book_item_lend_request.borrowed_by_id}"
            )

        return book_item_repo.lend_book_item(
            book_item=BookItemDomainModel.from_orm(book_item_lend_request)
        )


class BookItemLendRequest(BaseModel):
    id: int
    book_id: int
    book_item_id: str
    borrowed_by_id: int
