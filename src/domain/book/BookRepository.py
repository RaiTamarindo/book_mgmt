from abc import ABC, abstractmethod
from typing import List, Optional

from domain.book import Book

class BookRepository(ABC):
    @abstractmethod
    def save(self, book: Book) -> Book:
        pass

    @abstractmethod
    def find_all(self) -> List[Book]:
        pass

    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def delete_by_id(self, book_id: int) -> bool:
        pass