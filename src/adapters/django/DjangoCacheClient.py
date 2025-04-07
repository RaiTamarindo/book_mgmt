from typing import Any
from django.core.cache import cache

from adapters.contracts import CacheClient


class DjangoCacheClient(CacheClient):
    def get(self, key: str):
        return cache.get(key)

    def set(self, key: str, value: Any, timeout: int):
        cache.set(key, value, timeout)
