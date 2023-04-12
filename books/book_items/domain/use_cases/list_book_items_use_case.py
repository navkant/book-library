from dependency_injector.wiring import Provide

from books.book_items.data.book_item_abstract_repo import BookItemAbstractRepo


class ListBookItemUseCase:
    def execute(
        self,
        book_id,
        book_item_repo: BookItemAbstractRepo = Provide[
            "book_item_container.book_item_repo"
        ],
    ):
        return book_item_repo.list(book_id)
