import pytest
from books.services import enrich_book_data
from django.core.cache import cache
from django_redis import get_redis_connection

@pytest.fixture(autouse=True)
def clear_cache():
    get_redis_connection("default").flushdb()

@pytest.mark.django_db
def test_enrich_book_cache_miss(mocker):
    mock_fetch = mocker.patch(
        "books.enrichment.enrich_book_data",
        return_value={"language": "en", "pages": 300}
    )

    isbn = "9781234567897"
    result = enrich_book_data(isbn)

    assert result == {"language": "en", "pages": 300}
    assert mock_fetch.called  # API should be called on cache miss


@pytest.mark.django_db
def test_enrich_book_cache_hit(mocker):
    isbn = "9781234567897"
    cached_data = {"language": "en", "pages": 300}

    # Put data in cache manually
    cache_key = f"enrich_book_data:{isbn}"
    cache.set(cache_key, cached_data, timeout=3600)

    mock_fetch = mocker.patch(
        "books.enrichment.enrich_book_data"
    )

    result = enrich_book_data(isbn)

    assert result == cached_data
    mock_fetch.assert_not_called()  # Should not call the API again
