from django.utils import timezone

from books.book_items.data.book_item_abstract_repo import BookItemAbstractRepo
from books.book_items.domain.domain_models import (BookItemDomainModel,
                                                   BookItemsListDomainModel)
from books.models import BookItems


class BookItemDbRepo(BookItemAbstractRepo):
    def list(self, book_id) -> BookItemsListDomainModel:
        book_items = BookItems.objects.filter(book_id=book_id)

        return BookItemsListDomainModel(items=list(book_items))

    def lend_book_item(self, book_item: BookItemDomainModel) -> BookItemDomainModel:
        current_time = timezone.now()
        book_item_db = BookItems.objects.get(id=book_item.id)
        return_by = current_time + timezone.timedelta(weeks=1)
        book_item_db.borrowed_by_id = book_item.borrowed_by_id
        book_item_db.borrowed_at = current_time
        book_item_db.return_by = return_by
        book_item_db.save()

        return BookItemDomainModel.from_orm(book_item_db)
