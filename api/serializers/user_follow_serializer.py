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


class UserFollowInfoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='followee.id')  # hoặc 'follower.id' tùy view
    username = serializers.CharField(source='followee.username')
    email = serializers.EmailField(source='followee.email')
    followed_at = serializers.DateTimeField()

    class Meta:
        model = UserFollower
        fields = ['id', 'username', 'email', 'followed_at']
