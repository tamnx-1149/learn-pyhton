from rest_framework import serializers
from api.models import Comment, User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'author', 'created_at']
        read_only_fields = ['id', 'created_at']
