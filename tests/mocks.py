from typing import Any, Optional
from adapters.contracts import CacheClient


class MockCacheClient(CacheClient):
    def __init__(self):
        self.store = {}

    def get(self, key: str) -> Optional[Any]:
        return self.store.get(key)

    def set(self, key: str, value: Any, timeout: int) -> None:
        self.store[key] = value

