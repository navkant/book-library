from dependency_injector.wiring import Provide

from books.book.data.book_abstract_repo import BookAbstractRepo
from books.book.domain.domain_models import BookListDomainModel


class FilterBooksByGenreUseCase:
    def __init__(
        self, book_repo: BookAbstractRepo = Provide["book_container.book_repo"]
    ):
        self.book_repo = book_repo

    def execute(self, genre: str) -> BookListDomainModel:
        genres = genre.split(",")
        return self.book_repo.filter_books_by_genre(genres=genres)
