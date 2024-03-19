from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .converter import convert_query
from .elasticsearch import query_elasticsearch
from .serializers import QuerySerializer
from .tasks import log_query


class SearchView(APIView):
    def post(self, request: Request) -> Response:
        serializer = QuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        query = serializer.validated_data["query"]
        log_query.delay(request.user.username, query)

        converted_query = convert_query(query)
        results = query_elasticsearch(converted_query)
        return Response({"results": results})
