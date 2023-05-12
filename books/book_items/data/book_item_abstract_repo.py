import abc

from books.book_items.domain.domain_models import (
    BookItemDomainModel,
    BookItemsListDomainModel,
)


class BookItemAbstractRepo(abc.ABC):
    @abc.abstractmethod
    def list(self, book_id: int) -> BookItemsListDomainModel:
        pass

    @abc.abstractmethod
    def lend_book_item(self, book_item: BookItemDomainModel) -> BookItemDomainModel:
        """repo method to lend a book item to a user"""

    @abc.abstractmethod
    def check_borrowed_book_item(self, book_item_id: int, borrowed_by_id: int) -> bool:
        """check if given book item is borrowed by that user or not"""

    @abc.abstractmethod
    def list_borrowed_book_items(self, borrowed_by_id: int) -> BookItemsListDomainModel:
        """List all book items borrowed by a user"""

    @abc.abstractmethod
    def return_book_item(self, book_item: BookItemDomainModel) -> None:
        """Return a borrowed book item"""
