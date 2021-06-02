from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    body = models.TextField()
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.author} {self.title}"
