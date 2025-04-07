class EnrichedBook:
    def __init__(self, title: str = '', authors: list[str] = [], publisher: str = '', published_date: str = '', description: str = '',
                 page_count: int = 0, categories: list[str] = [], language: str = '', industry_identifiers: list[str] = [],
                 content_version: str = ''):
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.published_date = published_date
        self.description = description
        self.page_count = page_count
        self.categories = categories
        self.language = language
        self.industry_identifiers = industry_identifiers
        self.content_version = content_version

    def __repr__(self):
        return f"EnrichedBook(title={self.title}, authors={self.authors}, publisher={self.publisher}, " \
               f"published_date={self.published_date}, description={self.description})"
