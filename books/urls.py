from django.urls import include, path

from books.book.presentation import urls as book_urls
from books.book_items.presentation import urls as book_item_urls

urlpatterns = [
    path("books/", include(book_urls)),
    path("book_items/", include(book_item_urls)),
]
