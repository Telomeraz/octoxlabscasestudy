import pytest
from _pytest.fixtures import SubRequest

from django.contrib.auth.models import User

from .factories import UserFactory


@pytest.fixture
def user(request: SubRequest) -> User:
    data = getattr(request, "param", {})
    return UserFactory(**data)
