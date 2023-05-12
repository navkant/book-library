from typing import cast
from unittest import mock

from dependency_injector.wiring import Provide
from django.apps import apps
from django.test import SimpleTestCase

from books.apps import BooksConfig
from books.book.data.book_abstract_repo import BookAbstractRepo
from books.book.domain.domain_models import BookListDomainModel
from books.book.domain.use_cases.filter_books_by_genre_use_case import (
    FilterBooksByGenreUseCase,
)
from books.book.tests.factories import BookDomainModelFactory

books_app = cast(BooksConfig, apps.get_app_config("books"))


class ListAllBooksUseCaseTest(SimpleTestCase):
    def setUp(self) -> None:
        super(ListAllBooksUseCaseTest, self).setUp()
        self.mocked_book_repo = mock.Mock(BookAbstractRepo)
        books_app.inject_container.book_container.book_repo.override(
            self.mocked_book_repo
        )

    def test_execute(
        self,
        filter_books_by_genre: FilterBooksByGenreUseCase = Provide[
            "book_container.filter_books_by_genre_use_case"
        ],
    ):
        book_1 = BookDomainModelFactory(genre="suspense")
        book_2 = BookDomainModelFactory(genre="thriller")
        book_3 = BookDomainModelFactory()
        book_list = BookListDomainModel(items=[book_1, book_2])
        self.mocked_book_repo.filter_books_by_genre.return_value = book_list
        genres = "suspense, thriller"
        result = filter_books_by_genre.execute(genre="suspense, thriller")
        self.mocked_book_repo.filter_books_by_genre.assert_called_with(
            genres=genres.split(",")
        )
        self.assertEqual(len(result.items), 2)
