import abc

from books.book_items.domain.domain_models import (BookItemDomainModel,
                                                   BookItemsListDomainModel)


class BookItemAbstractRepo(abc.ABC):
    @abc.abstractmethod
    def list(self, book_id: int) -> BookItemsListDomainModel:
        pass

    @abc.abstractmethod
    def lend_book_item(self, book_item: BookItemDomainModel) -> BookItemDomainModel:
        """repo method to lend a book item to a user"""
