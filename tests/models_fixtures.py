"""
Фикстуры для использования в тестах
"""
from typing import Callable

import pytest

from backend.apps.companies.models import Company, Office
from backend.apps.users.models import User, Position, Skill, Language


@pytest.fixture(scope='session')
def default_username() -> str:
    return 'test_username'


@pytest.fixture(scope='session')
def default_password() -> str:
    return 'test_password'


@pytest.fixture(scope='session')
def default_company_name() -> str:
    return 'test_company'


@pytest.fixture(scope='session')
def default_position_name() -> str:
    return 'Manager'


@pytest.fixture(scope='session')
def default_skill_name() -> str:
    return 'python'


@pytest.fixture(scope='session')
def default_language_name() -> str:
    return 'english'


@pytest.fixture(scope='session')
def default_level() -> int:
    return 3


@pytest.fixture(scope='session')
def default_office_name() -> str:
    return 'test_office'


@pytest.fixture(scope='session')
def default_office_address() -> str:
    return 'test_address'


@pytest.fixture(scope='session')
def default_country() -> str:
    return 'BY'


@pytest.fixture()
def default_user(default_username: str, default_password: str) -> User:
    return User.objects.create(username=default_username, password=default_password)


@pytest.fixture()
def default_company(default_company_name: str) -> Company:
    return Company.objects.create(name=default_company_name)


@pytest.fixture()
def default_position(default_user: User, default_company: Company,
                     default_position_name: str) -> Position:
    return Position.objects.create(user=default_user,
                                   company=default_company,
                                   position=default_position_name)


@pytest.fixture()
def default_skill(default_user: User, default_skill_name: str,
                  default_level: int) -> Skill:
    return Skill.objects.create(user=default_user,
                                skill=default_skill_name,
                                level=default_level)


@pytest.fixture()
def default_language(default_user: User, default_language_name: str,
                     default_level: int) -> Language:
    return Language.objects.create(user=default_user,
                                   language=default_language_name,
                                   level=default_level)


@pytest.fixture()
def default_office(default_office_name: str, default_company: Company,
                   default_country: str, default_office_address: str) -> Office:
    return Office.objects.create(name=default_office_name,
                                 company=default_company,
                                 country=default_country,
                                 address=default_office_address)


@pytest.fixture()
def add_user(default_username: str, default_password: str) -> Callable:
    def _add_user(username: str = default_username, password: str = default_password,
                  is_active: bool = True, is_staff: bool = False) -> User:
        user = User.objects.create(username=username,
                                   password=password,
                                   is_active=is_active,
                                   is_staff=is_staff)
        return user

    return _add_user


@pytest.fixture()
def add_position(default_user: User,
                 default_company: Company,
                 default_position_name: str) -> Callable:
    def _add_position(user: User = default_user,
                      company: Company = default_company,
                      position: str = default_position_name,
                      is_active: bool = True) -> Position:
        return Position.objects.create(user=user, company=company,
                                       position=position, is_active=is_active)

    return _add_position


@pytest.fixture()
def add_office(default_office_name: str, default_company: Company,
               default_country: str, default_office_address: str) -> Callable:
    def _add_office(name: str = default_office_name, company: Company = default_company,
                    country: str = default_country, address: str = default_office_address,
                    is_active: bool = True) -> Office:
        return Office.objects.create(name=name, company=company, country=country,
                                     address=address, is_active=is_active)

    return _add_office
