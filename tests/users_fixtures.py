"""
Фикстуры для авторизации
"""
import pytest
from django.test.client import Client

from backend.apps.users.models import User


@pytest.fixture
def auth_headers_default(
    client: Client, default_user: User, default_username: str, default_password: str
) -> dict:
    """
    Возвращает jwt обычного пользователя
    """
    response = client.post(
        "/api/v1/token/",
        {
            "username": default_username,
            "password": default_password,
        },
        content_type="application/json",
    )
    auth_headers = {
        "HTTP_AUTHORIZATION": f"Bearer {response.data['access']}",
    }
    return auth_headers


@pytest.fixture
def auth_headers_admin(
    client: Client, admin_user_1: User, admin_username: str, admin_password: str
) -> dict:
    """
    Возвращает jwt пользователя с правами is_staff
    """
    response = client.post(
        "/api/v1/token/",
        {
            "username": admin_username,
            "password": admin_password,
        },
        content_type="application/json",
    )
    auth_headers = {
        "HTTP_AUTHORIZATION": f"Bearer {response.data['access']}",
    }
    return auth_headers
