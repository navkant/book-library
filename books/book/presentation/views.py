from dependency_injector.wiring import Provide
from rest_framework import response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from books.book.domain.use_cases.filter_books_by_genre_use_case import (
    FilterBooksByGenreUseCase,
)
from books.book.domain.use_cases.filter_books_by_name_use_case import (
    FilterBooksByNameUseCase,
)
from books.book.domain.use_cases.list_all_books_use_case import ListAllBooksUseCase
from books.book.presentation.types import BookFilterRequest, BookListResponse


class ListBooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(
        self,
        request,
        list_all_books_use_case: ListAllBooksUseCase = Provide[
            "book_container.list_books_use_case"
        ],
    ):
        books = list_all_books_use_case.execute()
        return response.Response(
            BookListResponse.from_orm(books).dict(), status=status.HTTP_200_OK
        )


class ListBooksByGenre(APIView):
    permission_classes = [IsAuthenticated]

    def post(
        self,
        request,
        get_books_by_genre_use_case: FilterBooksByGenreUseCase = Provide[
            "book_container.filter_books_by_genre_use_case"
        ],
    ):
        filter_request = BookFilterRequest.parse_obj(request.data)
        books = get_books_by_genre_use_case.execute(genre=filter_request.genre)
        return response.Response(
            BookListResponse.from_orm(books).dict(), status=status.HTTP_200_OK
        )


class ListBooksByName(APIView):
    permission_classes = [IsAuthenticated]

    def post(
        self,
        request,
        filter_books_by_name_use_case: FilterBooksByNameUseCase = Provide[
            "book_container.filter_books_by_name_use_case"
        ],
    ):
        filter_request = BookFilterRequest.parse_obj(request.data)
        books = filter_books_by_name_use_case.execute(name=filter_request.name)
        return response.Response(
            BookListResponse.from_orm(books).dict(), status=status.HTTP_200_OK
        )
