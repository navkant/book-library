import factory

from books.book.domain.domain_models import (BookDomainModel,
                                             BookListDomainModel)
from books.models import Book


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    summary = factory.Faker("pystr")
    isbn = factory.Faker("pystr")
    genre = factory.Faker("pystr")

    class Meta:
        model = Book


class BookDomainModelFactory(factory.Factory):
    title = factory.Faker("name")
    summary = factory.Faker("pystr")
    isbn = factory.Faker("pystr")
    genre = factory.Faker("pystr")

    class Meta:
        model = BookDomainModel


class BookListDomainModeFactory(factory.Factory):
    items = factory.List([factory.SubFactory(BookDomainModelFactory) for _ in range(3)])

    class Meta:
        model = BookListDomainModel
