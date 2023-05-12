from dependency_injector import containers, providers

from books.book_items.data.book_item_abstract_repo import BookItemAbstractRepo
from books.book_items.data.book_item_db_repo import BookItemDbRepo
from books.book_items.domain.use_cases.lend_book_item_use_case import (
    LendBookItemUseCase,
)
from books.book_items.domain.use_cases.list_book_items_use_case import (
    ListBookItemUseCase,
)
from books.book_items.domain.use_cases.list_borrowed_books import ListBorrowedBookItemsUseCase


class BookItemContainer(containers.DeclarativeContainer):
    book_item_repo = providers.Dependency(
        instance_of=BookItemAbstractRepo,
        default=BookItemDbRepo(),
    )
    list_book_item_use_case = providers.Factory(ListBookItemUseCase)
    lend_book_item_use_case = providers.Factory(LendBookItemUseCase)
    list_borrowed_book_items_use_case = providers.Factory(ListBorrowedBookItemsUseCase)
