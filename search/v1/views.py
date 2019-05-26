
from rest_framework.views import APIView
from search.v1.response import StandardSearchResponse
from search.v1.services.search_service import SearchService
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SearchView(APIView):
    """
    Deals with searching and sorting of results based on query params.
    user needs to be authenticated to perform this task
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        phone_number =request.query_params.get('phone_number')
        standard_search_response = StandardSearchResponse()

        if name and phone_number:
            return Response(standard_search_response.search_failed_response(400, "cannot search name and phone at once"), status=400)

        search_service = SearchService()
        if name:
            result_list_name = search_service.search_by_name(name)
            response_data = list(map(lambda x:x.get_profile, result_list_name))
            return Response(standard_search_response.search_success_response(response_data), status=200)

        if phone_number:
            result_list_phone = search_service.search_by_phone(phone_number)
            result_list_phone =  list(map(lambda x:x.get_profile, result_list_phone))
            return Response(standard_search_response.search_success_response(result_list_phone), status=200)

        return Response(standard_search_response.search_failed_response(403, "No query params provided to search"), status=403)
