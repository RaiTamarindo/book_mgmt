from injector import Binder, singleton
from adapters.contracts import CacheClient
from adapters.django import DjangoBookRepository, DjangoCacheClient
from adapters.google.GoogleBooksEnrichmentSerivce import GoogleBooksService
from domain.book.BookEnrichmentService import BookEnrichmentService
from domain.book.BookService import BookService
from domain.book.BookRepository import BookRepository

def configure(binder: Binder) -> None:
    # Bind the interfaces to implementations
    binder.bind(CacheClient, DjangoCacheClient, scope=singleton)
    binder.bind(BookRepository, DjangoBookRepository, scope=singleton)
    binder.bind(BookService, BookService, scope=singleton)
    binder.bind(BookEnrichmentService, GoogleBooksService, scope=singleton)
