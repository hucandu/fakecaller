from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from authentication.v1.serializers import RegisterUserSerializer, LoginUserSerializer
from authentication.v1.services.login import LoginService
from authentication.v1.services.registration import RegistrationService
from rest_framework.views import APIView
from authentication.v1.response import StandardAuthResponse

class RegistrationView(APIView):
    """
    Registers a user based on phone_number, name, email(optional) and password
    from user. Uses django User auth model
    """
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        registration_service = RegistrationService.register_user(serializer.data["phone_number"],
                                                                 serializer.data["name"],
                                                                 serializer.data["email"],
                                                                 serializer.data["password1"]
                                                                 )
        standard_auth_response = StandardAuthResponse()
        if registration_service:
            token = LoginService.login_user(
                serializer.data["phone_number"], serializer.data["password1"])
            return Response(standard_auth_response.login_success_response(token.key), status=200)
        return Response(standard_auth_response.login_failed_response(301, "Forbidden"), status=301)


class LoginView(APIView, StandardAuthResponse):
    """
    Login user based on username and password from user, uses
    django User auth model
    """
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = LoginService.login_user(
            serializer.data["phone_number"], serializer.data["password"])
        standard_auth_response = StandardAuthResponse()
        if token:
            return Response(standard_auth_response.login_success_response(token.key), status=200)
        return Response(standard_auth_response.login_failed_response(301, "Forbidden"), status=301)


class LogoutView(APIView):
    """
    Logout user based on username and password from user, uses
    django User auth model
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        standard_auth_response = StandardAuthResponse()
        return Response(standard_auth_response.logout_success_response(), status=200)
