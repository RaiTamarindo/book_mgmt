from abc import ABC, abstractmethod
from typing import Any, List, Optional
from domain.book.Book import Book

class CacheClient(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value from the cache by key."""
        pass

    @abstractmethod
    def set(self, key: str, value: Any, timeout: int) -> None:
        """Store a value in the cache with a timeout."""
        pass


