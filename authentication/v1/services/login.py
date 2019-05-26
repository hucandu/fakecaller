from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from core.models import PhoneBook


class LoginService():
    """
    This is responsible for all login related services
    that needs to be implemented before user gets notified that
    he is logged in
    """

    @classmethod
    def login_user(self, phone_number, password):
        user = authenticate(username=phone_number, password=password)
        if user:
            token , is_created= Token.objects.get_or_create(user=user)
            return token
        return None
