# views.py
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer
from books.services import create_book_with_enrichment

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        book = create_book_with_enrichment(self.request.data)
        serializer.instance = book

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
