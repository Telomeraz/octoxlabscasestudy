import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from django.contrib.auth.models import User
from django.urls import reverse

from search.views import SearchView

pytestmark = pytest.mark.django_db
request_factory = APIRequestFactory()


class TestSearchView:
    def test_post(self, user: User) -> None:
        data = {
            "query": "hostname = octoxlabs*",
        }
        request = request_factory.post(
            reverse("search"),
            data=data,
        )
        force_authenticate(request, user=user)
        response = SearchView.as_view()(request)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"]
