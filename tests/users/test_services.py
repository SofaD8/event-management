import pytest

from apps.users.models import User


@pytest.mark.django_db
def test_create_user_service():
    email = "new_sofa_dev@example.com"
    password = "super-secret-password"

    user = User.objects.create_user(email=email, password=password)

    assert user.email == email
    assert user.check_password(password) is True
    assert user.is_active is True
    assert user.is_staff is False


@pytest.mark.django_db
def test_cannot_create_duplicate_user(user):
    with pytest.raises(Exception):
        User.objects.create_user(email=user.email, password="another_password")
