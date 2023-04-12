from dependency_injector.wiring import Provide

from books.book.data.book_abstract_repo import BookAbstractRepo
from books.book.domain.domain_models import BookListDomainModel


class FilterBooksByNameUseCase:
    def __init__(
        self, book_repo: BookAbstractRepo = Provide["book_container.book_repo"]
    ):
        self.book_repo = book_repo

    def execute(self, name: str) -> BookListDomainModel:
        return self.book_repo.filter_books_by_name(name=name)
