import re
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

class RegisterUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30, required=False)
    password1 = serializers.CharField(max_length=30)
    password2 = serializers.CharField(max_length=30)

    def validate_phone_number(self, data):
        try:
            if data.isdigit() and int(data)>=10:
                return data
            else:
                raise exceptions.ValidationError("phone number is not valid")
        except Exception as e:
            raise exceptions.ValidationError("Enter a valid phone number")

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise exceptions.ValidationError("passwords do not match")
        return data





class LoginUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
