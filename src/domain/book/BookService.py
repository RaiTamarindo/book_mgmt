from typing import List, Optional

from injector import inject

from domain.book import BookEnrichmentService, BookRepository
from .Book import Book


class BookService:
    @inject
    def __init__(self, repository: BookRepository, enrichment_service: BookEnrichmentService):
        """
        Initialize the BookService.

        :param repository: An implementation of the BookRepository interface.
        :param enrichment_service: Service for enriching book data.
        """
        self.repository = repository
        self.enrichment_service = enrichment_service

    def create_book(self, book: Book) -> Book:
        """
        Create a new book and enrich its data.
        """
        enriched_data = self.enrichment_service.fetch_data(book.isbn)
        book.description = enriched_data.get("description", book.description)
        book.published_date = enriched_data.get("published_date", book.published_date)
        return self.repository.save(book)

    def get_books(self) -> List[Book]:
        """Retrieve all books."""
        return self.repository.find_all()

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Retrieve a book by its ID."""
        return self.repository.find_by_id(book_id)

    def update_book(self, book_id: int, updated_data: dict) -> Optional[Book]:
        """Update a book's details."""
        book = self.repository.find_by_id(book_id)
        if not book:
            return None

        for key, value in updated_data.items():
            setattr(book, key, value)

        return self.repository.save(book)

    def delete_book(self, book_id: int) -> bool:
        """Delete a book by its ID."""
        return self.repository.delete_by_id(book_id)
