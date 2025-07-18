from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


    def validate_email(self, value):
        user = self.instance  # user login
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
