from library_auth.exceptions import LibException
from rest_framework import status


class BookItemAlreadyLent(LibException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "This book item is already lent"
    default_code = "BOOK_ITEM_00001"
