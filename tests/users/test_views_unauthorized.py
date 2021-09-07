"""
Тесты views приложения users неавторизованным пользователем
"""
from typing import Callable

import pytest
from django.test.client import Client

from backend.apps.users.models import User, Language, Position, Skill


@pytest.mark.django_db
def test_users_create_unauthorized(client: Client) -> None:
    """
    Тест create пользователя неавторизованным пользователем
    """
    users = User.objects.all()
    assert len(users) == 0

    resp = client.post(
        "/api/v1/users/",
        {"username": "test_username", "password": "test_password"},
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["username"] == "test_username"

    users = User.objects.all()
    assert len(users) == 1


@pytest.mark.django_db
def test_users_create_invalid_data(client: Client) -> None:
    """
    Тест create пользователя с невалидными данными
    неавторизованным пользователем
    """
    users = User.objects.all()
    assert len(users) == 0
    resp = client.post(
        "/api/v1/users/",
        {
            "username": "test",
        },
        content_type="application/json",
    )
    assert resp.status_code == 400
    assert resp.data["password"] == ["This field is required."]

    users = User.objects.all()
    assert len(users) == 0


@pytest.mark.django_db
def test_users_list(client: Client, add_user: Callable) -> None:
    """
    Тест read списка пользователей неавторизованным пользователем
    """
    add_user(username="test1")
    add_user(username="test2")
    add_user(username="test3")
    users = User.objects.all()
    assert len(users) == 3

    resp = client.get("/api/v1/users/", content_type="application/json")
    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_users_read(client: Client, default_user: User) -> None:
    """
    Тест read полльзователя неавторизованным пользователем
    """
    resp = client.get(f"/api/v1/users/{default_user.id}/", content_type="application/json")
    assert resp.status_code == 200
    assert resp.data["username"] == default_user.username
    assert resp.data["id"] == default_user.id


@pytest.mark.django_db
def test_users_update(client: Client, default_user: User) -> None:
    """
    Тест update пользователя неавторизованным пользователем
    """
    resp = client.put(
        f"/api/v1/users/{default_user.id}/", {}, content_type="application/json"
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_partial_update(client: Client, default_user: User) -> None:
    """
    Тест partial_update пользователя неавторизованным пользователем
    """
    resp = client.patch(
        f"/api/v1/users/{default_user.id}/", {}, content_type="application/json"
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_language_list(client: Client, add_language: Callable) -> None:
    """
    Тест read списка языков неавторизованным пользователем
    """
    add_language(language="python")
    add_language(language="js")
    add_language(language="c")
    languages = Language.objects.all()
    assert len(languages) == 3
    resp = client.get("/api/v1/users/languages/", {}, content_type="application/json")
    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_users_language_create(client: Client) -> None:
    """
    Тест create языка неавторизованным пользователем
    """
    resp = client.post(
        "/api/v1/users/languages/",
        {"user": 1, "language": "string", "level": 0},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_language_read(client: Client, default_language: Language) -> None:
    """
    Тест read языка неавторизованным пользователем
    """
    resp = client.get(
        f"/api/v1/users/languages/{default_language.id}/", content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["id"] == default_language.id
    assert resp.data["language"] == default_language.language
    assert resp.data["user"]["id"] == default_language.user.id


@pytest.mark.django_db
def test_users_language_update(client: Client, default_language: Language) -> None:
    """
    Тест update языка неавторизованным пользователем
    """
    resp = client.put(
        f"/api/v1/users/languages/{default_language.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_language_partial_update(client: Client, default_language: Language) -> None:
    """
    Тест partial_update языка неавторизованным пользователем
    """
    resp = client.patch(
        f"/api/v1/users/languages/{default_language.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_position_list(client: Client, add_position: Callable) -> None:
    """
    Тест read списка должностей неавторизованным пользователем
    """
    add_position()
    add_position()
    add_position()
    positions = Position.objects.all()
    assert len(positions) == 3
    resp = client.get("/api/v1/users/positions/", {}, content_type="application/json")
    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_users_position_create(client: Client) -> None:
    """
    Тест create должности неавторизованным пользователем
    """
    resp = client.post(
        "/api/v1/users/positions/",
        {
            "user": 1,
            "position": "string",
            "company": 1,
        },
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_positions_read(client: Client, default_position: Position) -> None:
    """
    Тест read должности неавторизованным пользователем
    """
    resp = client.get(
        f"/api/v1/users/positions/{default_position.id}/", content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["id"] == default_position.id
    assert resp.data["position"] == default_position.position
    assert resp.data["user"]["id"] == default_position.user.id
    assert resp.data["company"]["id"] == default_position.company.id


@pytest.mark.django_db
def test_users_position_update(client: Client, default_position: Position) -> None:
    """
    Тест update должности неавторизованным пользователем
    """
    resp = client.put(
        f"/api/v1/users/positions/{default_position.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_position_partial_update(client: Client, default_position: Position) -> None:
    """
    Тест partial_update должности неавторизованным пользователем
    """
    resp = client.patch(
        f"/api/v1/users/positions/{default_position.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_skill_list(client: Client, add_skill: Callable) -> None:
    """
    Тест read списка навыков неавторизованным пользователем
    """
    add_skill()
    add_skill()
    add_skill()
    skills = Skill.objects.all()
    assert len(skills) == 3
    resp = client.get("/api/v1/users/skills/", {}, content_type="application/json")
    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_users_skill_create(client: Client) -> None:
    """
    Тест create навыка неавторизованным пользователем
    """
    resp = client.post(
        "/api/v1/users/skills/",
        {"user": 1, "skill": "string", "level": 0},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_skill_read(client: Client, default_skill: Skill) -> None:
    """
    Тест read навыка неавторизованным пользователем
    """
    resp = client.get(
        f"/api/v1/users/skills/{default_skill.id}/", content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["id"] == default_skill.id
    assert resp.data["skill"] == default_skill.skill
    assert resp.data["user"]["id"] == default_skill.user.id


@pytest.mark.django_db
def test_users_skill_update(client: Client, default_skill: Skill) -> None:
    """
    Тест update навыка неавторизованным пользователем
    """
    resp = client.put(
        f"/api/v1/users/skills/{default_skill.id}/", {}, content_type="application/json"
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_users_skill_partial_update(client: Client, default_skill: Skill) -> None:
    """
    Тест partial_update навыка неавторизованным пользователем
    """
    resp = client.patch(
        f"/api/v1/users/skills/{default_skill.id}/", {}, content_type="application/json"
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."
