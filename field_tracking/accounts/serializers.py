from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    user_type = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

