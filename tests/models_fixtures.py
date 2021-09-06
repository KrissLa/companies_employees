import pytest
from backend.apps.users.models import User, Position, Skill, Language
from backend.apps.companies.models import Company, Office


@pytest.fixture(scope='session')
def default_username():
    return 'test_username'


@pytest.fixture(scope='session')
def default_password():
    return 'test_password'


@pytest.fixture(scope='session')
def default_company_name():
    return 'test_company'


@pytest.fixture(scope='session')
def default_position_name():
    return 'Manager'


@pytest.fixture(scope='session')
def default_skill_name():
    return 'python'


@pytest.fixture(scope='session')
def default_language_name():
    return 'english'


@pytest.fixture(scope='session')
def default_level():
    return 3


@pytest.fixture(scope='session')
def default_office_name():
    return 'test_office'


@pytest.fixture(scope='session')
def default_office_address():
    return 'test_address'


@pytest.fixture(scope='session')
def default_country():
    return 'BY'


@pytest.fixture()
def default_user(default_username, default_password):
    return User.objects.create(username=default_username, password=default_password)
    # return user


@pytest.fixture()
def default_company(default_company_name):
    return Company.objects.create(name=default_company_name)


@pytest.fixture()
def default_position(default_user, default_company, default_position_name):
    return Position.objects.create(user=default_user, company=default_company, position=default_position_name)


@pytest.fixture()
def default_skill(default_user, default_skill_name, default_level):
    return Skill.objects.create(user=default_user, skill=default_skill_name, level=default_level)


@pytest.fixture()
def default_language(default_user, default_language_name, default_level):
    return Language.objects.create(user=default_user, language=default_language_name, level=default_level)


@pytest.fixture()
def default_office(default_office_name, default_company, default_country, default_office_address):
    return Office.objects.create(name=default_office_name, company=default_company,
                                 country=default_country, address=default_office_address)


@pytest.fixture()
def add_user(default_username, default_password):
    def _add_user(username=default_username, password=default_password, is_active=True, is_staff=False):
        user = User.objects.create(username=username, password=password, is_active=is_active, is_staff=is_staff)
        return user

    return _add_user


@pytest.fixture()
def add_position(default_user, default_company, default_position_name):
    def _add_position(user=default_user, company=default_company,
                      position=default_position_name, is_active=True):
        return Position.objects.create(user=user, company=company,
                                       position=position, is_active=is_active)

    return _add_position


#
#
# @pytest.fixture(scope='function')
# def add_company():
#     def _add_company(name='Company', is_active=True):
#         company = Company.objects.create(name=name, is_active=is_active)
#         return company
#     return _add_company

@pytest.fixture()
def add_office(default_office_name, default_company, default_country, default_office_address):
    def _add_office(name=default_office_name, company=default_company,
                    country=default_country, address=default_office_address,
                    is_active=True):
        return Office.objects.create(name=name, company=company, country=country, address=address, is_active=is_active)

    return _add_office
