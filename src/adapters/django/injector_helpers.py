# injector_helpers.py
from injector import inject, Injector
from django.views import View

from domain.book.BookService import BookService

class InjectedView(View):
    @inject
    def __init__(self, book_service: BookService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book_service = book_service
