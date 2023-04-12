from abc import ABC, abstractmethod
from typing import List

from books.book.domain.domain_models import BookListDomainModel


class BookAbstractRepo(ABC):
    @abstractmethod
    def list_all_books(self) -> BookListDomainModel:
        """Method to return all books"""

    @abstractmethod
    def filter_books_by_genre(self, genres: List[str]) -> BookListDomainModel:
        """method to return books by given genres"""

    @abstractmethod
    def filter_books_by_name(self, name: str) -> BookListDomainModel:
        """method to filter books by name"""
