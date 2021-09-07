"""
Тесты views приложения companies неавторизованным пользователем
"""
from typing import Callable

import pytest
from django.test.client import Client

from backend.apps.companies.models import Company, Office


@pytest.mark.django_db
def test_companies_list(client: Client, add_company: Callable) -> None:
    """
    Тест read списка компаний неавторизованным пользователем
    """
    add_company()
    add_company()
    add_company()
    companies = Company.objects.all()
    assert len(companies) == 3
    resp = client.get("/api/v1/companies/", content_type="application/json")
    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_companies_create(client: Client) -> None:
    """
    Тест create компании неавторизованным пользователем
    """
    resp = client.post(
        "/api/v1/companies/",
        {
            "name": "Company_name",
        },
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_companies_read(client: Client, default_company: Company) -> None:
    """
    Тест read компании неавторизованным пользователем
    """
    resp = client.get(
        f"/api/v1/companies/{default_company.id}/", content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["id"] == default_company.id
    assert resp.data["name"] == default_company.name


@pytest.mark.django_db
def test_companies_update(client: Client, default_company: Company) -> None:
    """
    Тест update компании неавторизованным пользователем
    """
    resp = client.put(
        f"/api/v1/companies/{default_company.id}/", {}, content_type="application/json"
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_companies_partial_update(client: Client, default_company: Company) -> None:
    """
    Тест partial_update компании неавторизованным пользователем
    """
    resp = client.patch(
        f"/api/v1/companies/{default_company.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_companies_partnership_add(
    client: Client, default_company: Company, add_company: Callable
) -> None:
    """
    Тест partnership_add_partner компании неавторизованным пользователем
    """
    company1 = add_company(name="Компания")
    resp = client.post(
        f"/api/v1/companies/{default_company.id}/partnership/add/",
        {"id": company1.id},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_companies_partnership_remove(
    client: Client, default_company: Company, add_company: Callable
) -> None:
    """
    Тест partnership_remove_partner компании неавторизованным пользователем
    """
    company1 = add_company(name="Компания")
    default_company.partners_companies.add(company1)
    default_company.save()
    resp = client.post(
        f"/api/v1/companies/{default_company.id}/partnership/remove/",
        {"id": company1.id},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_companies_offices_list(client: Client, add_office: Callable) -> None:
    """
    Тест read списка офисов неавторизованным пользователем
    """
    add_office()
    add_office()
    add_office()
    offices = Office.objects.all()
    assert len(offices) == 3
    resp = client.get("/api/v1/companies/offices/", content_type="application/json")
    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_companies_offices_create(client: Client, default_company: Company) -> None:
    """
    Тест create офиса неавторизованным пользователем
    """
    resp = client.post(
        "/api/v1/companies/offices/",
        {
            "name": "string",
            "country": "AF",
            "address": "string",
            "company": default_company.id,
        },
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_companies_offices_read(client: Client, default_office: Office) -> None:
    """
    Тест read офиса неавторизованным пользователем
    """
    resp = client.get(
        f"/api/v1/companies/offices/{default_office.id}/", content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["id"] == default_office.id
    assert resp.data["name"] == default_office.name
    assert resp.data["country"] == default_office.country
    assert resp.data["address"] == default_office.address
    assert resp.data["company"]["id"] == default_office.company.id


@pytest.mark.django_db
def test_companies_offices_update(client: Client, default_office: Office) -> None:
    """
    Тест update офиса неавторизованным пользователем
    """
    resp = client.put(
        f"/api/v1/companies/offices/{default_office.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_companies_offices_partial_update(client: Client, default_office: Office) -> None:
    """
    Тест partial_update офиса неавторизованным пользователем
    """
    resp = client.patch(
        f"/api/v1/companies/offices/{default_office.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 401
    assert resp.data["detail"] == "Authentication credentials were not provided."
