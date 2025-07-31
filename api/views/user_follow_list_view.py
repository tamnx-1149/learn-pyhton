from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from api.models import UserFollower
from django.contrib.auth import get_user_model

from api.serializers.user_follow_serializer import UserFollowInfoSerializer

User = get_user_model()


class UserFollowListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user;
        followings = UserFollower.objects.filter(follower=user)
        serializer = UserFollowInfoSerializer(followings, many=True)
        return Response(serializer.data)
