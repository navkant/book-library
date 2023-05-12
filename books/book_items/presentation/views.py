from dependency_injector.wiring import Provide
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from books.book_items.domain.use_cases.lend_book_item_use_case import (
    BookItemLendRequest,
    LendBookItemUseCase,
)
from books.book_items.domain.use_cases.list_book_items_use_case import (
    ListBookItemUseCase,
)
from books.book_items.domain.use_cases.list_borrowed_books import ListBorrowedBookItemsUseCase
from books.book_items.presentation.types import BookItemResponse, BookItemsListResponse
from ddtrace import tracer


class ListBookItemsView(APIView):
    permission_classes = [IsAuthenticated]

    @tracer.wrap(service="my_new_resource", resource="book_item")
    def get(
        self,
        request,
        book_id: int,
        list_book_item_use_case: ListBookItemUseCase = Provide[
            "book_item_container.list_book_item_use_case"
        ],
    ):
        book_items = list_book_item_use_case.execute(book_id)

        return Response(
            BookItemsListResponse(
                items=book_items.items,
            ).dict(),
            status=status.HTTP_200_OK,
        )


class LendBookItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(
        self,
        request,
        lend_book_item_use_case: LendBookItemUseCase = Provide[
            "book_item_container.lend_book_item_use_case"
        ],
    ):
        book_item_lend_request = BookItemLendRequest.parse_obj(request.data)

        book_item = lend_book_item_use_case.execute(
            book_item_lend_request=book_item_lend_request
        )

        return Response(
            BookItemResponse.from_orm(book_item).dict(),
            status=status.HTTP_200_OK,
        )


class ListBorrowedBookItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(
        self,
        request,
        list_borrowed_book_items_use_case: ListBorrowedBookItemsUseCase = Provide["book_item_container.list_borrowed_book_items_use_case"]
    ):
        borrowed_by_id = request.user.id
        book_item_list = list_borrowed_book_items_use_case.execute(borrowed_by_id=borrowed_by_id)

        return Response(
            BookItemsListResponse(
                items=book_item_list.items,
            ).dict(),
            status=status.HTTP_200_OK,
        )
