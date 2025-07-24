from django.contrib.auth.models import User
from django.db import models


class ArticleFavorite(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name='article_set')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_set')
    favorite_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'api_article_favorites'
        unique_together = ('article_id', 'user_id')
        indexes = [
            models.Index(fields=['article_id']),
            models.Index(fields=['user_id']),
        ]

    def __str__(self):
        return f"{self.article_id.title} follows {self.user_id.username}"
