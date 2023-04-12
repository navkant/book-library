import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    summary = models.TextField(blank=True, null=True)
    isbn = models.CharField(blank=False, null=False, max_length=50)
    genre = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class BookItems(models.Model):
    book = models.ForeignKey(
        Book,
        blank=False,
        null=False,
        related_name="book_items",
        on_delete=models.CASCADE,
    )
    book_item_id = models.CharField(max_length=40, null=False, default=uuid.uuid4)
    borrowed_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name="borrowed_books",
        on_delete=models.DO_NOTHING,
    )
    borrowed_at = models.DateTimeField(null=True, blank=True)
    return_by = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} ({self.book_item_id})"

    class Meta:
        verbose_name = "Book Items"
        verbose_name_plural = verbose_name
