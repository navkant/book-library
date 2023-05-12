from dependency_injector import containers, providers

from books.book.data.book_abstract_repo import BookAbstractRepo
from books.book.data.book_db_repo import BookDbRepo
from books.book.domain.use_cases.filter_books_by_genre_use_case import (
    FilterBooksByGenreUseCase,
)
from books.book.domain.use_cases.filter_books_by_name_use_case import (
    FilterBooksByNameUseCase,
)
from books.book.domain.use_cases.list_all_books_use_case import ListAllBooksUseCase


class BookContainer(containers.DeclarativeContainer):
    book_repo = providers.Dependency(
        instance_of=BookAbstractRepo,
        default=BookDbRepo(),
    )
    list_books_use_case = providers.Factory(ListAllBooksUseCase)
    filter_books_by_genre_use_case = providers.Factory(FilterBooksByGenreUseCase)
    filter_books_by_name_use_case = providers.Factory(FilterBooksByNameUseCase)
