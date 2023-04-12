from typing import List

from books.book.data.book_abstract_repo import BookAbstractRepo
from books.book.domain.domain_models import (BookDomainModel,
                                             BookListDomainModel)
from books.models import Book


class BookDbRepo(BookAbstractRepo):
    def list_all_books(self) -> BookListDomainModel:
        books = Book.objects.all()
        return BookListDomainModel(items=list(map(BookDomainModel.from_orm, books)))

    def filter_books_by_genre(self, genres: List[str]) -> BookListDomainModel:
        books = list()
        for genre in genres:
            books.extend(Book.objects.filter(genre__icontains=genre))

        return BookListDomainModel(items=list(map(BookDomainModel.from_orm, books)))

    def filter_books_by_name(self, name: str) -> BookListDomainModel:
        books = Book.objects.filter(title__icontains=name)
        return BookListDomainModel(items=list(map(BookDomainModel.from_orm, books)))
