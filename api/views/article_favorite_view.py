from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from api.models import Article, ArticleFavorite
from api.serializers import ArticleFavoriteSerializer


class ArticleFavoriteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)

        # Kiểm tra xem đã favorite chưa
        if ArticleFavorite.objects.filter(user=request.user, article=article).exists():
            return Response({"detail": "Article already favorited."}, status=status.HTTP_400_BAD_REQUEST)

        favorite = ArticleFavorite.objects.create(user=request.user, article=article)
        serializer = ArticleFavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, slug, pk):
        favorite = get_object_or_404(ArticleFavorite, id=pk)

        # Delete the favorite if it exists
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
