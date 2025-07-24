from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import UserFollower

User = get_user_model()


class UserFollowSerializer(serializers.ModelSerializer):
    follower_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='follower')
    followee_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='followee')

    class Meta:
        model = UserFollower
        fields = ['id', 'follower_id', 'followee_id', 'followed_at']
        read_only_fields = ['followed_at']
