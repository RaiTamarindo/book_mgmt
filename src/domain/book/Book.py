from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    description: Optional[str]
    published_date: Optional[date]
