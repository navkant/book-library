from dependency_injector import containers, providers

from books.book.inject import BookContainer
from books.book_items.inject import BookItemContainer


class BooksContainer(containers.DeclarativeContainer):
    book_container = providers.Container(BookContainer)
    book_item_container = providers.Container(BookItemContainer)
