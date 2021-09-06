"""
Тесты для моделей приложения users
"""
import pytest

from backend.apps.companies.models import Company
from backend.apps.users.models import User, Language, Skill, Position


@pytest.mark.django_db
def test_user_model(
    default_user: User, default_username: str, default_password: str
) -> None:
    """
    Тест модели User
    """
    assert default_user.username == default_username
    assert default_user.check_password(default_password)
    assert not default_user.first_name
    assert not default_user.last_name
    assert not default_user.email
    assert not default_user.patronymic
    assert not default_user.age
    assert not default_user.is_staff
    assert default_user.is_active
    assert default_user.date_joined
    assert default_user.created_at
    assert default_user.updated_at
    assert str(default_user) == default_user.username


@pytest.mark.django_db
def test_position_model(
    default_company: Company,
    default_user: User,
    default_position: Position,
    default_position_name: str,
) -> None:
    """
    Тест модели Position
    """
    assert default_position.is_active
    assert default_position.created_at
    assert default_position.updated_at
    assert default_position.position == default_position_name
    assert default_position.user == default_user
    assert default_position.company == default_company
    assert default_user.user_companies.all().count() == 1
    assert default_company.employees.all().count() == 1
    assert default_company.number_of_employees == 1
    assert (
        str(default_position) == f"{default_position_name} - "
        f"{default_position.user.username} "
        f"в {default_position.company.name}"
    )


@pytest.mark.django_db
def test_skill_model(
    default_user: User, default_skill: Skill, default_skill_name: str, default_level: int
) -> None:
    """
    Тест модели Skill
    """
    assert default_skill.user == default_user
    assert default_skill.skill == default_skill_name
    assert default_skill.level == default_level
    assert default_skill.is_active
    assert default_skill.updated_at
    assert default_skill.created_at
    assert default_user.skills.all().count() == 1
    assert (
        str(default_skill) == f"{default_skill.skill} - "
        f"{default_skill.level} - "
        f"{default_skill.user.username}"
    )


@pytest.mark.django_db
def test_language_model(
    default_user: User,
    default_language: Language,
    default_level: int,
    default_language_name: str,
) -> None:
    """
    Тест модели Language
    """
    assert default_language.user == default_user
    assert default_language.language == default_language_name
    assert default_language.level == default_level
    assert default_language.is_active
    assert default_language.updated_at
    assert default_language.created_at
    assert default_user.languages.all().count() == 1
    assert (
        str(default_language) == f"{default_language.language} - "
        f"{default_language.level} - "
        f"{default_language.user.username}"
    )
