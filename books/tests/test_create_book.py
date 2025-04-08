import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from books.models import Book

@pytest.mark.django_db
def test_create_book_with_mocked_enrichment(mocker):
    # Mock the enrichment function
    mocker.patch(
        "books.services.enrich_book_data",
        return_value={"language": "en", "pages": 250}
    )

    client = APIClient()
    url = reverse("book-list-create")
    data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "1234567890123",
        "description": "Test Description",
        "published_date": "2023-01-01"
        # missing pages and language on purpose
    }

    response = client.post(url, data, format="json")
    assert response.status_code == 201

    book = Book.objects.get(isbn="1234567890123")
    assert book.pages == 250
    assert book.language == "en"
