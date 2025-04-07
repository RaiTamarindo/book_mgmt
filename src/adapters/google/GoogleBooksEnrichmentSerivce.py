import hashlib
from injector import inject
import requests

from adapters.contracts import CacheClient
from domain.book import BookEnrichmentService, EnrichedBook

class GoogleBooksService(BookEnrichmentService):
    @inject
    def __init__(self, cache_client: CacheClient):
        """
        Initialize the GoogleBooksService.

        :param cache_client: An implementation of the CacheClient interface.
        """
        self.cache_client = cache_client
    
    def fetch_data(self, isbn: str) -> EnrichedBook:
        cache_key = hashlib.md5(f"google-books:{isbn}".encode()).hexdigest()

        cached_data = self.cache_client.get(cache_key)
        if cached_data:
            return cached_data

        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            book_info = data['items'][0]['volumeInfo']
            enriched_book = EnrichedBook(
                title = book_info.get('title'),
                authors = book_info.get('authors', []),
                publisher = book_info.get('publisher', ''),
                published_date = book_info.get('publishedDate', ''),
                description = book_info.get('description', ''),
                page_count = book_info.get('pageCount', 0),
                categories = book_info.get('categories', []),
                language = book_info.get('language', ''),
                industry_identifiers = book_info.get('industryIdentifiers', []),
                content_version = book_info.get('contentVersion', ''),
            )

            self.cache_client.set(cache_key, enriched_book, ttl=24 * 3600) # 24 hours
            return enriched_book

        return EnrichedBook() 
