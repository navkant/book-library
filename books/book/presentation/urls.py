from django.urls import path

from books.book.presentation import views

urlpatterns = [
    path(r"", views.ListBooksView.as_view(), name="list-books"),
    path(f"genre/", views.ListBooksByGenre.as_view(), name="books_by_genre"),
    path(f"book_name/", views.ListBooksByName.as_view(), name="books_by_name"),
]
