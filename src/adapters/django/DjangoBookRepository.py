from typing import List, Optional
from adapters.django.models import BookModel
from domain.book import BookRepository
from domain.book.Book import Book


class DjangoBookRepository(BookRepository):
    def save(self, book: Book) -> Book:
        book_instance = BookModel.objects.update_or_create(
            id=book.id, defaults=book.__dict__
        )[0]
        return Book(**book_instance.__dict__)

    def find_all(self) -> List[Book]:
        return [Book(**obj.__dict__) for obj in BookModel.objects.all()]

    def find_by_id(self, book_id: int) -> Optional[Book]:
        try:
            obj = BookModel.objects.get(id=book_id)
            return Book(**obj.__dict__)
        except BookModel.DoesNotExist:
            return None

    def delete_by_id(self, book_id: int) -> bool:
        deleted, _ = BookModel.objects.filter(id=book_id).delete()
        return deleted > 0
