from rest_framework import status
from rest_framework.test import APIRequestFactory

from django.urls import reverse

from converter.views import ConvertQueryView

request_factory = APIRequestFactory()


class TestConvertQueryView:
    def test_post(self) -> None:
        data = {
            "query": "hostname = octoxlabs*",
        }
        request = request_factory.post(
            reverse("convert_query"),
            data=data,
        )
        response = ConvertQueryView.as_view()(request)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["result"] == {
            "wildcard": {
                "hostname": "octoxlabs*",
            },
        }

    def test_post_if_query_is_exact_match(self) -> None:
        data = {
            "query": "hostname = octoxlabs",
        }
        request = request_factory.post(
            reverse("convert_query"),
            data=data,
        )
        response = ConvertQueryView.as_view()(request)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["result"] == {
            "match": {
                "hostname": "octoxlabs",
            },
        }
