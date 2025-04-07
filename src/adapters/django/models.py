from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "books"

    def __str__(self):
        return f"{self.title} by {self.author}"
