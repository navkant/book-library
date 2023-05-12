from typing import cast
from unittest import mock

from dependency_injector.wiring import Provide
from django.apps import apps
from django.test import SimpleTestCase

from books.apps import BooksConfig
from books.book.data.book_abstract_repo import BookAbstractRepo
from books.book.domain.use_cases.list_all_books_use_case import ListAllBooksUseCase
from books.book.tests.factories import BookDomainModelFactory, BookListDomainModeFactory

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
        list_all_books_use_case: ListAllBooksUseCase = Provide[
            "book_container.list_books_use_case"
        ],
    ):
        book_list = BookListDomainModeFactory()
        self.mocked_book_repo.list_all_books.return_value = book_list
        result = list_all_books_use_case.execute()
        self.mocked_book_repo.list_all_books.assert_called_with()
        self.assertEqual(len(result.items), 3)
