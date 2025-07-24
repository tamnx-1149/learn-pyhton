from django.contrib.auth.models import User
from django.db import models

class UserFollower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'api_user_followers'
        unique_together = ('follower', 'followee')
        indexes = [
            models.Index(fields=['follower']),
            models.Index(fields=['followee']),
        ]

    def __str__(self):
        return f"{self.follower.username} follows {self.followee.username}"