from django.test import TestCase

from books.book.data.book_db_repo import BookDbRepo
from books.book.domain.domain_models import (BookDomainModel,
                                             BookListDomainModel)
from books.book.tests.factories import BookFactory


class BookDbRepoTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.db_repo = BookDbRepo()

    def test_list_all_books(self):
        book_1 = BookFactory()
        book_2 = BookFactory()
        book_3 = BookFactory()

        books = self.db_repo.list_all_books()
        self.assertEqual(len(books.items), 3)
        self.assertEqual(
            books,
            BookListDomainModel(
                items=[
                    BookDomainModel.from_orm(book_1),
                    BookDomainModel.from_orm(book_2),
                    BookDomainModel.from_orm(book_3),
                ]
            ),
        )

    def test_filter_books_by_genre(self):
        genre_name = "random_genre"
        book_1 = BookFactory(genre=genre_name)
        book_2 = BookFactory()

        books = self.db_repo.filter_books_by_genre(genres=[genre_name])
        self.assertEqual(len(books.items), 1)
        self.assertEqual(
            books,
            BookListDomainModel(
                items=[
                    BookDomainModel.from_orm(book_1),
                ]
            ),
        )

    def test_filter_book_by_name(self):
        book_name = "Book Name"
        book_1 = BookFactory(title=book_name)
        book_2 = BookFactory()

        books = self.db_repo.filter_books_by_name(name=book_name)
        self.assertEqual(len(books.items), 1)
        self.assertEqual(
            books,
            BookListDomainModel(
                items=[
                    BookDomainModel.from_orm(book_1),
                ]
            ),
        )
