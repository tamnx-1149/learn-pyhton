from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils.text import slugify

from api.models import Article, Tag
from api.serializers import ArticleSerializer
from django.shortcuts import get_object_or_404


class ArticleView(APIView):
    def get(self, request, pk=None):
        if pk:
            # Lấy chi tiết bài viết
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Lấy danh sách bài viết
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        tag_names = request.pop('tagList', [])
        slug = slugify(request.get('title', ''))
        request['slug'] = slug
        serializer = ArticleSerializer(data=request.data)
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            serializer.tags.add(tag)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
