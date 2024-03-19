from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .converter import convert_query_to_es_format
from .serializers import QuerySerializer


class ConvertQueryView(APIView):
    def post(self, request: Request) -> Response:
        serializer = QuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        query = serializer.validated_data["query"]

        converted_query = convert_query_to_es_format(query)
        return Response({"result": converted_query})
