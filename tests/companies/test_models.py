import pytest


@pytest.mark.django_db
def test_company_model(default_company, default_company_name):
    assert default_company.name == default_company_name
    assert default_company.number_of_offices == 0
    assert default_company.number_of_employees == 0
    assert default_company.partners_companies.all().count() == 0
    assert default_company.is_active
    assert default_company.created_at
    assert default_company.updated_at
    assert str(default_company) == f'Компания {default_company.name}'


@pytest.mark.django_db
def test_company_get_number_of_offices(default_company, add_office):
    add_office()
    add_office()
    add_office(is_active=False)
    assert default_company.offices.all().count() == 3
    assert default_company.get_number_of_offices() == 2
    assert default_company.number_of_offices == 2


@pytest.mark.django_db
def test_company_get_number_of_employees_1(default_company, default_user, add_position):
    add_position()
    add_position()
    add_position()
    assert default_company.employees.all().count() == 3
    assert default_company.number_of_employees == 1


@pytest.mark.django_db
def test_company_get_number_of_employees_3(default_company, add_user, add_position):
    user_1 = add_user(username='aaa')
    user_2 = add_user(username='bbb')
    user_3 = add_user(username='ccc')
    add_position(user=user_1)
    add_position(user=user_2)
    add_position(user=user_3, is_active=False)
    assert default_company.employees.all().count() == 3
    assert default_company.number_of_employees == 2


@pytest.mark.django_db
def test_office_model(default_company, default_office, default_office_name,
                      default_country, default_office_address):
    assert default_office.name == default_office_name
    assert default_office.company == default_company
    assert default_office.country == default_country
    assert default_office.address == default_office_address
    assert default_office.is_active
    assert default_office.created_at
    assert default_office.updated_at
    assert default_company.offices.all().count() == 1
    assert default_company.number_of_offices == 1
    assert str(default_office) == f'Офис {default_office.name} компании {default_office.company.name}'
