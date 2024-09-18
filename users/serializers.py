from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'coordinates']

    def create(self, validated_data):

        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # password hash kar raha hu django's own algorthim 
        user.save()
        return user
