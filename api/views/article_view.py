from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.fillter import ArticleFilter
from api.models import Article, Tag
from api.serializers import ArticleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from django.db import connection

class ArticleView(APIView):
    @method_decorator(cache_page(60*5))  # cache 5 phút
    def get(self, request, slug=None):
        version = request.version  #
        print(version)
        if slug:
            # Lấy chi tiết bài viết
            article = get_object_or_404(Article, slug=slug)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Lấy danh sách bài viết
            articles = Article.objects.all()
            # Filtering articles based on query parameters
            filterset = ArticleFilter(request.GET, queryset=articles)
            if filterset.is_valid():
                queryset = filterset.qs
            else:
                return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

            ordering = request.query_params.get('ordering')
            allowed_ordering_fields = ['created_at', 'title', 'author']
            if ordering:
                field = ordering.lstrip('-')
                if field in allowed_ordering_fields:
                    articles = queryset.order_by(ordering)
            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(articles, request)

        serializer = ArticleSerializer(page, many=True)
        print(connection.queries[-1]['sql'])

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
