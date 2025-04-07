from django.urls import path
from .views import BookView

urlpatterns = [
    path('books/', BookView.as_view(), name='get_books'),
    # path('books/', BookView.create_book, name='create_book'),
    # path('books/<int:book_id>/', BookView.get_book, name='get_book'),
    # path('books/<int:book_id>/update/', BookView.update_book, name='update_book'),
    # path('books/<int:book_id>/delete/', BookView.delete_book, name='delete_book'),
]
