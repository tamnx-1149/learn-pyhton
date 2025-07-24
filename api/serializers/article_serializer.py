from rest_framework import serializers
from api.models import Article, Tag
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    tagList = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    tags = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name'
    )

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'description', 'body', 'slug',
            'tagList', 'tags', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        tag_names = validated_data.pop('tagList', [])

        author = User.objects.get(pk=1)

        article = Article.objects.create(author=author, **validated_data)
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            article.tags.add(tag)
        return article

    def update(self, instance, validated_data):
        tag_names = validated_data.pop('tagList', None)
        if tag_names is not None:
            instance.tags.clear()
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return super().update(instance, validated_data)
