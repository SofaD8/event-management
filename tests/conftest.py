import pytest
from rest_framework.test import APIClient

from apps.users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client(api_client, db):
    user = User.objects.create_user(email="test@example.com", password="password123")
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def user(db):
    return User.objects.create_user(
        email="test_user@example.com",
        password="password123"
    )
