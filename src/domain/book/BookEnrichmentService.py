from abc import ABC, abstractmethod

from domain.book import EnrichedBook


class BookEnrichmentService(ABC):
    @abstractmethod
    def fetch_data(self, isbn: str) -> EnrichedBook:
        """Retrieve book data from the isbn number."""
        pass