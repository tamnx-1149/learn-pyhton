from django.db import models


class Article(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    body = models.TextField()
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name='articles')
    tags = models.ManyToManyField("Tag", related_name='articles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
