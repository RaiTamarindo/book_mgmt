from books.enrichment import enrich_book_data
from books.models import Book

def create_book_with_enrichment(data: dict) -> Book:
    isbn = data.get("isbn")
    enrichment = {}

    if isbn and (not data.get("pages") or not data.get("language")):
        enrichment = enrich_book_data(isbn)

    clean_data = {k: v for k, v in data.items() if k in [f.name for f in Book._meta.fields]}
    enriched_data = {
        **clean_data,
        "pages": data.get("pages") or enrichment.get("pages"),
        "language": data.get("language") or enrichment.get("language"),
    }

    return Book.objects.create(**enriched_data)
