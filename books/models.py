from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    published_date = models.DateField()
    pages = models.PositiveIntegerField(blank=True)
    language = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
