"""
Фикстуры для использования в тестах
"""
from typing import Callable

import pytest

from backend.apps.companies.models import Company, Office
from backend.apps.users.models import User, Position, Skill, Language


@pytest.fixture(scope="session")
def default_username() -> str:
    """
    Возвращает стандартный тестовый username
    """
    return "test_username"


@pytest.fixture(scope="session")
def admin_username() -> str:
    """
    Возвращает тестовый username пользователя is_staff
    """
    return "admin_username"


@pytest.fixture(scope="session")
def default_password() -> str:
    """
    Возвращает стандартный тестовый пароль
    """
    return "test_password"


@pytest.fixture(scope="session")
def admin_password() -> str:
    """
    Возвращает тестовый пароль пользователя is_staff
    """
    return "admin_password"


@pytest.fixture(scope="session")
def default_company_name() -> str:
    """
    Возвращает стандартное тестовое название компании
    """
    return "test_company"


@pytest.fixture(scope="session")
def default_position_name() -> str:
    """
    Возвращает стандартное тестовое название должности
    """
    return "Manager"


@pytest.fixture(scope="session")
def default_skill_name() -> str:
    """
    Возвращает стандартное тестовое название навыка
    """
    return "python"


@pytest.fixture(scope="session")
def default_language_name() -> str:
    """
    Возвращает стандартное тестовое название языка
    """
    return "english"


@pytest.fixture(scope="session")
def default_level() -> int:
    """
    Возвращает стандартный тестовый уровень
    """
    return 3


@pytest.fixture(scope="session")
def default_office_name() -> str:
    """
    Возвращает стандартное тестовое название офиса
    """
    return "test_office"


@pytest.fixture(scope="session")
def default_office_address() -> str:
    """
    Возвращает стандартный тестовый адрес
    """
    return "test_address"


@pytest.fixture(scope="session")
def default_country() -> str:
    """
    Возвращает стандартный объект country
    """
    return "BY"


@pytest.fixture()
def default_user(default_username: str, default_password: str) -> User:
    """
    Возвращает стандартный объект User
    """
    return User.objects.create(username=default_username, password=default_password)


@pytest.fixture()
def admin_user_1(admin_username: str, admin_password: str) -> User:
    """
    Возвращает объект User с правами is_staff
    """
    return User.objects.create(
        username=admin_username, password=admin_password, is_staff=True
    )


@pytest.fixture()
def default_company(default_company_name: str) -> Company:
    """
    Возвращает стандартный объект Company
    """
    return Company.objects.create(name=default_company_name)


@pytest.fixture()
def default_position(
    default_user: User, default_company: Company, default_position_name: str
) -> Position:
    """
    Возвращает стандартный объект Position
    """
    return Position.objects.create(
        user=default_user, company=default_company, position=default_position_name
    )


@pytest.fixture()
def default_skill(
    default_user: User, default_skill_name: str, default_level: int
) -> Skill:
    """
    Возвращает стандартный объект Skill
    """
    return Skill.objects.create(
        user=default_user, skill=default_skill_name, level=default_level
    )


@pytest.fixture()
def default_language(
    default_user: User, default_language_name: str, default_level: int
) -> Language:
    """
    Возвращает стандартный объект Language
    """
    return Language.objects.create(
        user=default_user, language=default_language_name, level=default_level
    )


@pytest.fixture()
def default_office(
    default_office_name: str,
    default_company: Company,
    default_country: str,
    default_office_address: str,
) -> Office:
    """
    Возвращает стандартный объект Office
    """
    return Office.objects.create(
        name=default_office_name,
        company=default_company,
        country=default_country,
        address=default_office_address,
    )


@pytest.fixture()
def add_user(default_username: str, default_password: str) -> Callable:
    """
    Возвращает функцию создающую объект User
    """

    def _add_user(
        username: str = default_username,
        password: str = default_password,
        is_active: bool = True,
        is_staff: bool = False,
    ) -> User:
        user = User.objects.create(
            username=username, password=password, is_active=is_active, is_staff=is_staff
        )
        return user

    return _add_user


@pytest.fixture()
def add_position(
    default_user: User, default_company: Company, default_position_name: str
) -> Callable:
    """
    Возвращает функцию создающую объект Position
    """

    def _add_position(
        user: User = default_user,
        company: Company = default_company,
        position: str = default_position_name,
        is_active: bool = True,
    ) -> Position:
        return Position.objects.create(
            user=user, company=company, position=position, is_active=is_active
        )

    return _add_position


@pytest.fixture()
def add_office(
    default_office_name: str,
    default_company: Company,
    default_country: str,
    default_office_address: str,
) -> Callable:
    """
    Возвращает функцию создающую объект Office
    """

    def _add_office(
        name: str = default_office_name,
        company: Company = default_company,
        country: str = default_country,
        address: str = default_office_address,
        is_active: bool = True,
    ) -> Office:
        return Office.objects.create(
            name=name,
            company=company,
            country=country,
            address=address,
            is_active=is_active,
        )

    return _add_office


@pytest.fixture()
def add_language(
    default_user: User,
    default_language_name: str,
    default_level: int,
) -> Callable:
    """
    Возвращает функцию создающую объект Language
    """

    def _add_language(
        user: User = default_user,
        language: str = default_language_name,
        level: int = default_level,
        is_active: bool = True,
    ) -> Language:
        return Language.objects.create(
            user=user, language=language, level=level, is_active=is_active
        )

    return _add_language


@pytest.fixture()
def add_skill(
    default_user: User,
    default_skill_name: str,
    default_level: int,
) -> Callable:
    """
    Возвращает функцию создающую объект Skill
    """

    def _add_skill(
        user: User = default_user,
        skill: str = default_skill_name,
        level: int = default_level,
        is_active: bool = True,
    ) -> Skill:
        return Skill.objects.create(
            user=user, skill=skill, level=level, is_active=is_active
        )

    return _add_skill


@pytest.fixture()
def add_company(default_company_name: str) -> Callable:
    """
    Возвращает функцию создающую объект Company
    """

    def _add_company(
        name: str = default_company_name,
        is_active: bool = True,
    ) -> Skill:
        return Company.objects.create(name=name, is_active=is_active)

    return _add_company
