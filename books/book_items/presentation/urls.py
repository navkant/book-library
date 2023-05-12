from django.urls import path

from books.book_items.presentation import views

urlpatterns = [
    path("<int:book_id>/", views.ListBookItemsView.as_view()),
    path("lend_book_item/", views.LendBookItemView.as_view()),
    path("list_borrowed_book_items/", views.ListBorrowedBookItemsView.as_view()),
]
