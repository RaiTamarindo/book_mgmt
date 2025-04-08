import logging
from utils.cache import redis_cache
from django.conf import settings
import requests

logger = logging.getLogger(__name__)

@redis_cache(ttl_seconds=3600)
def enrich_book_data(isbn: str) -> dict:
    base_url = f"https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"isbn:{isbn}"}
    if hasattr(settings, "GOOGLE_BOOKS_API_KEY"):
        params["key"] = settings.GOOGLE_BOOKS_API_KEY
    
    data = {}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        logger.info("Google Books request: %s | Params: %s | Status: %s | Response: %s", response.url, params, response.status_code, data)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error("Google Books API request failed: %s", e)
        return {}

    if "items" not in data or not data["items"]:
        return {}

    volume_info = data["items"][0]["volumeInfo"]
    return {
        "pages": volume_info.get("pageCount"),
        "language": volume_info.get("language"),
        "title": volume_info.get("title"),
        "author": ", ".join(volume_info.get("authors", [])),
        "description": volume_info.get("description"),
        "published_date": volume_info.get("publishedDate"),
    }
