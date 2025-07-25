from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import ArticleFavorite, Article

User = get_user_model();


class ArticleFavoriteSerializer(serializers.ModelSerializer):
    article_id = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), source='article')
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')

    class Meta:
        model = ArticleFavorite
        fields = ['id', 'article_id', 'user_id', 'favorite_at']
        read_only_fields = ['favorite_at']
