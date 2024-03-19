import pytest
from rest_framework.test import APIRequestFactory

from django.contrib.auth.models import User
from django.urls import reverse

from octo_auth.octo_auth import OctoAuthentication

pytestmark = pytest.mark.django_db
request_factory = APIRequestFactory()


class TestOctoAuthentication:
    def test_authenticate(self) -> None:
        user = User.objects.create_user(
            username="admin",
            password="admin",
        )
        headers = {"HTTP_AUTHORIZATION": "Octoxlabs YWRtaW46YWRtaW4="}
        data = {
            "query": "hostname = octoxlabs*",
        }
        request = request_factory.post(
            reverse("search"),
            data=data,
            **headers,
        )

        user_, dummy = OctoAuthentication().authenticate(request)

        assert user == user_
