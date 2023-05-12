from books.book_items.data.book_item_abstract_repo import BookItemAbstractRepo
from dependency_injector.wiring import Provide
from books.book_items.domain.domain_models import BookItemsListDomainModel


class ListBorrowedBookItemsUseCase:
    def execute(
        self,
        borrowed_by_id: int,
        book_item_repo: BookItemAbstractRepo = Provide["book_item_container.book_item_repo"]
    ) -> BookItemsListDomainModel:
        return book_item_repo.list_borrowed_book_items(borrowed_by_id=borrowed_by_id)
