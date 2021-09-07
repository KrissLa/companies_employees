"""
Фикстуры для авторизации
"""
import pytest
from django.test.client import Client
from loguru import logger

from backend.apps.users.models import User


@pytest.fixture
def jwt_token(
    client: Client, default_user: User, default_username: str, default_password: str
) -> str:
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
    return response.data["access"]


@pytest.fixture
def jwt_token_admin(
    client: Client, admin_user: User, admin_username: str, admin_password: str
) -> str:
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
    logger.info(response.data["access"])
    return response.data["access"]
