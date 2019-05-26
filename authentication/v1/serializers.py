from rest_framework import serializers


class RegisterUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30, required=False)
    password1 = serializers.CharField(max_length=30)
    password2 = serializers.CharField(max_length=30)



class LoginUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
