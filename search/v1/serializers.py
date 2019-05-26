from rest_framework import serializers


class ProfileListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=30)
    is_spam = serializers.CharField(max_length=100)
