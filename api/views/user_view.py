from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.models import User
from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer


class UserView(APIView):

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
