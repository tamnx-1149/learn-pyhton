from rest_framework import serializers
from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    tagList = serializers.ListField(
        child=serializers.CharField(max_length=50),
        write_only=True,
        required=False
    )

    class Meta:
        model = Article
        fields = '__all__'
