from django.db import models

from django.contrib.auth.models import User


class Comment(models.Model):
    body = models.TextField()
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.article.title}'
