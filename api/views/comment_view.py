from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.models import Article, Comment
from django.shortcuts import get_object_or_404

from api.serializers.comment_serializer import CommentSerializer


class CommentView(APIView):

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, pk):
        article = get_object_or_404(Article, slug=slug)
        comment = get_object_or_404(Comment, id=pk, article=article)

        # Optional: Check if the user is the author of the comment
        if comment.author != request.user:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response({'detail': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
