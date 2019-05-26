from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from mark_spam.v1.services.spam_services import NumberSpamService
from mark_spam.v1.response import SpamAuthResponse

class MarkSpamView(APIView):
    """
    Mark a number as spam
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
    	user = request.user
    	phone = request.data.get("phone_number")
    	numberspamservice = NumberSpamService.mark_given_number_as_spam(user, phone)
    	standard_auth_response = SpamAuthResponse()
    	if numberspamservice:
    		return Response(standard_auth_response.spam_success_response())

    	return Response(standard_auth_response.spam_failed_response())

    		


