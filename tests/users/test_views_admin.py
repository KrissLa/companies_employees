"""
Тесты views приложения users админом
"""

import pytest
from django.test.client import Client

from backend.apps.companies.models import Company
from backend.apps.users.models import User, Language, Position, Skill


@pytest.mark.django_db
def test_users_create_admin(client: Client, auth_headers_admin: dict) -> None:
    """
    Тест create пользователя админом
    """

    users = User.objects.all()
    assert len(users) == 1
    resp = client.post(
        "/api/v1/users/",
        {"username": "test_username", "password": "test_password"},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 201
    assert resp.data["username"] == "test_username"
    assert not resp.data.get("password", None)

    users = User.objects.all()
    assert len(users) == 2


@pytest.mark.django_db
def test_users_update_admin(
    client: Client, auth_headers_admin: dict, default_user: User
) -> None:
    """
    Тест update пользователя админом
    """
    resp = client.put(
        f"/api/v1/users/{default_user.id}/",
        {"username": "string", "email": "user@example.com", "password": "string"},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["username"] == "string"
    assert resp.data["email"] == "user@example.com"
    assert not resp.data.get("password", None)


@pytest.mark.django_db
def test_users_partial_update_admin(
    client: Client, auth_headers_admin: dict, default_user: User
) -> None:
    """
    Тест partial update пользователя админом
    """
    resp = client.patch(
        f"/api/v1/users/{default_user.id}/",
        {"is_active": False},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert not resp.data["is_active"]


@pytest.mark.django_db
def test_users_language_create(
    client: Client, default_user: User, auth_headers_admin: dict
) -> None:
    """
    Тест create языка неавторизованным админом
    """
    resp = client.post(
        "/api/v1/users/languages/",
        {
            "user": default_user.id,
            "language": "string",
            "level": 5,
        },
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 201
    assert resp.data["user"] == default_user.id
    assert resp.data["language"] == "string"
    assert resp.data["level"] == 5


@pytest.mark.django_db
def test_users_language_update(
    client: Client, auth_headers_admin: dict, default_language: Language
) -> None:
    """
    Тест update языка админом
    """
    resp = client.put(
        f"/api/v1/users/languages/{default_language.id}/",
        {
            "language": "Python",
            "level": 7,
        },
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["language"] == "Python"
    assert resp.data["level"] == 7
    assert resp.data["id"] == default_language.id


@pytest.mark.django_db
def test_users_language_partial_update(
    client: Client, auth_headers_admin: dict, default_language: Language
) -> None:
    """
    Тест partial update языка админом
    """
    resp = client.patch(
        f"/api/v1/users/languages/{default_language.id}/",
        {
            "level": 1,
        },
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["level"] == 1
    assert resp.data["id"] == default_language.id


@pytest.mark.django_db
def test_users_position_create(
    client: Client, default_user: User, default_company: Company, auth_headers_admin: dict
) -> None:
    """
    Тест create должности админом
    """
    resp = client.post(
        "/api/v1/users/positions/",
        {
            "user": default_user.id,
            "position": "string",
            "company": default_company.id,
        },
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 201
    assert resp.data["position"] == "string"
    assert resp.data["user"] == default_user.id
    assert resp.data["company"] == default_company.id


@pytest.mark.django_db
def test_users_position_update(
    client: Client, default_position: Position, auth_headers_admin: dict
) -> None:
    """
    Тест update должности админом
    """
    resp = client.put(
        f"/api/v1/users/positions/{default_position.id}/",
        {"position": "JS"},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["position"] == "JS"
    assert resp.data["user"] == default_position.user.id
    assert resp.data["company"] == default_position.company.id


@pytest.mark.django_db
def test_users_position_partial_update(
    client: Client, default_position: Position, auth_headers_admin: dict
) -> None:
    """
    Тест partial update должности админом
    """
    resp = client.patch(
        f"/api/v1/users/positions/{default_position.id}/",
        {"is_active": False},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert not resp.data["is_active"]


@pytest.mark.django_db
def test_users_skill_create(
    client: Client, default_user: User, auth_headers_admin: dict
) -> None:
    """
    Тест create навыка админом
    """
    resp = client.post(
        "/api/v1/users/skills/",
        {"user": default_user.id, "skill": "string", "level": 1},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 201
    assert resp.data["skill"] == "string"
    assert resp.data["level"] == 1
    assert resp.data["user"] == default_user.id


@pytest.mark.django_db
def test_users_skill_update(
    client: Client, default_skill: Skill, auth_headers_admin: dict
) -> None:
    """
    Тест update навыка админом
    """
    resp = client.put(
        f"/api/v1/users/skills/{default_skill.id}/",
        {"skill": "string", "level": 9, "is_active": False},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["skill"] == "string"
    assert resp.data["level"] == 9
    assert not resp.data["is_active"]


@pytest.mark.django_db
def test_users_skill_partial_update(
    client: Client, default_skill: Skill, auth_headers_admin: dict
) -> None:
    """
    Тест partial update навыка админом
    """
    resp = client.patch(
        f"/api/v1/users/skills/{default_skill.id}/",
        {"skill": "JS", "is_active": False},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["skill"] == "JS"
    assert not resp.data["is_active"]
