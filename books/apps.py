from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "books"
    inject_container = None

    def ready(self):
        from books import book, book_items
        from books.inject import BooksContainer

        self.inject_container = BooksContainer()
        self.inject_container.wire(
            packages=[
                book,
                book_items,
            ]
        )
