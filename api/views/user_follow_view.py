from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from api.models import UserFollower
from api.serializers import UserFollowSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFollowAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        target_user = get_object_or_404(User, username=username)
        current_user = request.user
        if current_user == target_user:
            return Response({'detail': 'Bạn không thể tự theo dõi chính mình.'}, status=status.HTTP_400_BAD_REQUEST)

        follow_relation, created = UserFollower.objects.get_or_create(
            follower=current_user,
            followee=target_user
        )

        if created:
            return Response({'detail': f'Follow {username}.'}, status=status.HTTP_201_CREATED)
        else:
            follow_relation.delete()
            return Response({'detail': f'Unfollow {username}.'}, status=status.HTTP_204_NO_CONTENT)

