from dependency_injector.wiring import Provide

from books.book.data.book_abstract_repo import BookAbstractRepo
from books.book.domain.domain_models import BookListDomainModel


class ListAllBooksUseCase:
    def __init__(
        self, book_repo: BookAbstractRepo = Provide["book_container.book_repo"]
    ):
        self.book_repo = book_repo

    def execute(self) -> BookListDomainModel:
        return self.book_repo.list_all_books()
