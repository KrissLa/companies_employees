"""
Тесты views приложения users авторизованным пользователем
"""
from typing import Callable

import pytest
from django.test.client import Client
from loguru import logger

from backend.apps.companies.models import Company
from backend.apps.users.models import User, Language, Position, Skill


@pytest.mark.django_db
def test_users_create_authorized(client: Client, auth_headers_default: dict) -> None:
    """
    Тест create пользователя админом
    """

    users = User.objects.all()
    assert len(users) == 1
    resp = client.post(
        "/api/v1/users/",
        {"username": "test_username", "password": "test_password"},
        content_type="application/json",
        **auth_headers_default,
    )
    logger.info(resp.data)
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."

    users = User.objects.all()
    assert len(users) == 1


@pytest.mark.django_db
def test_users_update_self_authorized(
    client: Client, auth_headers_default: dict, default_user: User
) -> None:
    """
    Тест update пользователя самим собой
    """
    resp = client.put(
        f"/api/v1/users/{default_user.id}/",
        {"username": "string", "email": "user@example.com", "password": "string"},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 200
    assert resp.data["username"] == "string"
    assert resp.data["email"] == "user@example.com"
    assert not resp.data.get("password", None)


@pytest.mark.django_db
def test_users_update_authorized(
    client: Client, auth_headers_default: dict, default_user: User, add_user: Callable
) -> None:
    """
    Тест update пользователя другим пользователем
    """
    new_user = add_user(username="new")
    resp = client.put(
        f"/api/v1/users/{new_user.id}/",
        {"username": "string", "email": "user@example.com", "password": "string"},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_partial_update_self_authorized(
    client: Client, auth_headers_default: dict, default_user: User
) -> None:
    """
    Тест partial update пользователя самим собой
    """
    resp = client.patch(
        f"/api/v1/users/{default_user.id}/",
        {
            "email": "user@example.com",
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 200
    assert resp.data["username"] == default_user.username
    assert resp.data["email"] == "user@example.com"


@pytest.mark.django_db
def test_users_partial_update_authorized(
    client: Client, auth_headers_default: dict, default_user: User, add_user: Callable
) -> None:
    """
    Тест partial update пользователя другим пользователем
    """
    new_user = add_user(username="new")
    resp = client.patch(
        f"/api/v1/users/{new_user.id}/",
        {
            "email": "user@example.com",
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_language_create_self_authorized(
    client: Client, default_user: User, auth_headers_default: dict
) -> None:
    """
    Тест create языка самим собой
    """
    resp = client.post(
        "/api/v1/users/languages/",
        {
            "user": default_user.id,
            "language": "string",
            "level": 5,
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 201
    assert resp.data["user"] == default_user.id
    assert resp.data["language"] == "string"
    assert resp.data["level"] == 5


@pytest.mark.django_db
def test_users_language_create_authorized(
    client: Client, default_user: User, auth_headers_default: dict, add_user: Callable
) -> None:
    """
    Тест create языка другим пользователем
    """
    new_user = add_user(username="new")
    resp = client.post(
        "/api/v1/users/languages/",
        {
            "user": new_user.id,
            "language": "string",
            "level": 5,
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_language_update_self_authorized(
    client: Client, auth_headers_default: dict, default_language: Language
) -> None:
    """
    Тест update языка самим собой
    """
    resp = client.put(
        f"/api/v1/users/languages/{default_language.id}/",
        {
            "language": "Python",
            "level": 7,
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 200
    assert resp.data["language"] == "Python"
    assert resp.data["level"] == 7
    assert resp.data["id"] == default_language.id


@pytest.mark.django_db
def test_users_language_update_authorized(
    client: Client, auth_headers_default: dict, add_user: Callable, add_language: Callable
) -> None:
    """
    Тест update языка другим пользователем
    """
    new_user = add_user(username="new")
    new_language = add_language(user=new_user)
    resp = client.put(
        f"/api/v1/users/languages/{new_language.id}/",
        {
            "language": "Python",
            "level": 7,
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_language_partial_update_self_authorized(
    client: Client, auth_headers_default: dict, default_language: Language
) -> None:
    """
    Тест partial update языка самим собой
    """
    resp = client.patch(
        f"/api/v1/users/languages/{default_language.id}/",
        {
            "language": "Python",
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 200
    assert resp.data["language"] == "Python"
    assert resp.data["level"] == default_language.level
    assert resp.data["id"] == default_language.id


@pytest.mark.django_db
def test_users_language_partial_update_authorized(
    client: Client, auth_headers_default: dict, add_user: Callable, add_language: Callable
) -> None:
    """
    Тест partial update языка другим пользователем
    """
    new_user = add_user(username="new")
    new_language = add_language(user=new_user)
    resp = client.patch(
        f"/api/v1/users/languages/{new_language.id}/",
        {
            "language": "Python",
            "level": 7,
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_skill_create_self_authorized(
    client: Client, default_user: User, auth_headers_default: dict
) -> None:
    """
    Тест create навыка самому себе
    """
    resp = client.post(
        "/api/v1/users/skills/",
        {"user": default_user.id, "skill": "string", "level": 1},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 201
    assert resp.data["skill"] == "string"
    assert resp.data["level"] == 1
    assert resp.data["user"] == default_user.id


@pytest.mark.django_db
def test_users_skill_create_authorized(
    client: Client, default_user: User, auth_headers_default: dict, add_user: Callable
) -> None:
    """
    Тест create навыка другому пользователю
    """
    new_user = add_user(username="new")
    resp = client.post(
        "/api/v1/users/skills/",
        {"user": new_user.id, "skill": "string", "level": 1},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_skill_update_self_authorized(
    client: Client, default_skill: Skill, auth_headers_default: dict
) -> None:
    """
    Тест update навыка самому себе
    """
    resp = client.put(
        f"/api/v1/users/skills/{default_skill.id}/",
        {"skill": "string", "level": 9, "is_active": False},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 200
    assert resp.data["skill"] == "string"
    assert resp.data["level"] == 9
    assert not resp.data["is_active"]


@pytest.mark.django_db
def test_users_skill_update_authorized(
    client: Client, auth_headers_default: dict, add_skill: Callable, add_user: Callable
) -> None:
    """
    Тест update навыка другому пользователю
    """
    new_user = add_user(username="new")
    new_skill = add_skill(user=new_user)
    resp = client.put(
        f"/api/v1/users/skills/{new_skill.id}/",
        {"skill": "string", "level": 9, "is_active": False},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_skill_partial_update_self_authorized(
    client: Client, default_skill: Skill, auth_headers_default: dict
) -> None:
    """
    Тест partial update навыка самому себе
    """
    resp = client.patch(
        f"/api/v1/users/skills/{default_skill.id}/",
        {"level": 9, "is_active": False},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 200
    assert resp.data["level"] == 9
    assert not resp.data["is_active"]


@pytest.mark.django_db
def test_users_skill_partial_update_authorized(
    client: Client, auth_headers_default: dict, add_skill: Callable, add_user: Callable
) -> None:
    """
    Тест partial update навыка другому пользователю
    """
    new_user = add_user(username="new")
    new_skill = add_skill(user=new_user)
    resp = client.put(
        f"/api/v1/users/skills/{new_skill.id}/",
        {"level": 9},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_position_create_authorized(
    client: Client,
    default_user: User,
    default_company: Company,
    auth_headers_default: dict,
) -> None:
    """
    Тест create должности пользователем
    """
    resp = client.post(
        "/api/v1/users/positions/",
        {
            "user": default_user.id,
            "position": "string",
            "company": default_company.id,
        },
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_position_update_authorized(
    client: Client, default_position: Position, auth_headers_default: dict
) -> None:
    """
    Тест update должности пользователем
    """
    resp = client.put(
        f"/api/v1/users/positions/{default_position.id}/",
        {"position": "JS"},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_users_position_partial_update_authorized(
    client: Client, default_position: Position, auth_headers_default: dict
) -> None:
    """
    Тест partial update должности пользователем
    """
    resp = client.patch(
        f"/api/v1/users/positions/{default_position.id}/",
        {"is_active": False},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."
