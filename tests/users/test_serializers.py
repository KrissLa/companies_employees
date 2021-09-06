"""
Тесты для сериализаторов приложения users
"""
import pytest

from backend.api.v1.users import serializers
from backend.apps.companies.models import Company
from backend.apps.users.models import User


@pytest.mark.django_db
def test_user_create_update_serializer() -> None:
    """
    Тест UserCreateUpdateSerializer с валидными данными
    """
    valid_data = {
        "username": "asd",
        "first_name": "string",
        "last_name": "sdfsd",
        "patronymic": "dsfsd",
        "age": 21,
        "email": "user@example.com",
        "password": "sdfdsf",
        "is_active": True,
    }
    serializer = serializers.UserCreateUpdateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    valid_data.pop("password", None)
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_user_create_update_serializer() -> None:
    """
    Тест UserCreateUpdateSerializer с невалидными данными
    """
    invalid_serializer_data = {
        "username": "asd",
        "first_name": "string",
        "last_name": "sdfsd",
        "patronymic": "dsfsd",
        "age": 21,
        "email": "user@example.com",
        "is_active": True,
    }
    serializer = serializers.UserCreateUpdateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"password": ["This field is required."]}


@pytest.mark.django_db
def test_position_create_serializer(default_user: User, default_company: Company) -> None:
    """
    Тест PositionCreateSerializer с валидными данными
    """
    valid_data = {
        "user": default_user.id,
        "position": "string",
        "company": default_company.id,
        "is_active": True,
    }
    serializer = serializers.PositionCreateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data.get("user") == default_user
    assert serializer.validated_data.get("company") == default_company
    assert serializer.validated_data.get("position") == valid_data.get("position")
    assert serializer.validated_data.get("is_active") == valid_data.get("is_active")
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_position_create_serializer(default_user: User) -> None:
    """
    Тест PositionCreateSerializer с невалидными данными
    """
    invalid_serializer_data = {
        "user": default_user.id,
        "position": "string",
    }
    serializer = serializers.PositionCreateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"company": ["This field is required."]}


@pytest.mark.django_db
def test_position_update_serializer() -> None:
    """
    Тест PositionUpdateSerializer с валидными данными
    """
    valid_data = {
        "position": "sdfsdfsdf",
        "is_active": True,
    }
    serializer = serializers.PositionUpdateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_position_update_serializer() -> None:
    """
    Тест PositionUpdateSerializer с невалидными данными
    """
    invalid_serializer_data = {"is_active": True}
    serializer = serializers.PositionUpdateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"position": ["This field is required."]}


@pytest.mark.django_db
def test_skill_create_serializer(default_user: User) -> None:
    """
    Тест SkillCreateSerializer с валидными данными
    """
    valid_data = {
        "user": default_user.id,
        "skill": "string",
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.SkillCreateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data.get("user") == default_user
    assert serializer.validated_data.get("skill") == valid_data["skill"]
    assert serializer.validated_data.get("level") == valid_data.get("level")
    assert serializer.validated_data.get("is_active") == valid_data.get("is_active")
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_skill_create_serializer() -> None:
    """
    Тест SkillCreateSerializer с невалидными данными
    """
    invalid_serializer_data = {
        "skill": "string",
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.SkillCreateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"user": ["This field is required."]}


@pytest.mark.django_db
def test_skill_update_serializer() -> None:
    """
    Тест SkillUpdateSerializer с валидными данными
    """
    valid_data = {
        "skill": "string",
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.SkillUpdateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_skill_update_serializer() -> None:
    """
    Тест SkillUpdateSerializer с невалидными данными
    """
    invalid_serializer_data = {
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.SkillUpdateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"skill": ["This field is required."]}


@pytest.mark.django_db
def test_language_create_serializer(default_user: User) -> None:
    """
    Тест LanguageCreateSerializer с валидными данными
    """
    valid_data = {
        "user": default_user.id,
        "language": "string",
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.LanguageCreateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data.get("user") == default_user
    assert serializer.validated_data.get("language") == valid_data["language"]
    assert serializer.validated_data.get("level") == valid_data.get("level")
    assert serializer.validated_data.get("is_active") == valid_data.get("is_active")
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_language_create_serializer() -> None:
    """
    Тест LanguageCreateSerializer с невалидными данными
    """
    invalid_serializer_data = {
        "language": "string",
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.LanguageCreateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"user": ["This field is required."]}


@pytest.mark.django_db
def test_language_update_serializer() -> None:
    """
    Тест LanguageUpdateSerializer с валидными данными
    """
    valid_data = {
        "language": "string",
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.LanguageUpdateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_language_update_serializer() -> None:
    """
    Тест LanguageUpdateSerializer с невалидными данными
    """
    invalid_serializer_data = {
        "level": 1,
        "is_active": True,
    }
    serializer = serializers.LanguageUpdateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"language": ["This field is required."]}
