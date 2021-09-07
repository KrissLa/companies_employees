"""
Тесты views приложения companies админом
"""
from typing import Callable

import pytest
from django.test.client import Client

from backend.apps.companies.models import Company, Office


@pytest.mark.django_db
def test_companies_create(client: Client, auth_headers_admin: dict) -> None:
    """
    Тест create компании админом
    """
    resp = client.post(
        "/api/v1/companies/",
        {
            "name": "Company_name",
        },
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "Company_name"


@pytest.mark.django_db
def test_companies_update(
    client: Client, default_company: Company, auth_headers_admin: dict
) -> None:
    """
    Тест update компании админом
    """
    resp = client.put(
        f"/api/v1/companies/{default_company.id}/",
        {
            "name": "Company_name1",
        },
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "Company_name1"


@pytest.mark.django_db
def test_companies_partial_update(
    client: Client, default_company: Company, auth_headers_admin: dict
) -> None:
    """
    Тест partial_update компании админом
    """
    resp = client.put(
        f"/api/v1/companies/{default_company.id}/",
        {"name": "Company_name112", "is_active": False},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "Company_name112"
    assert not resp.data["is_active"]


@pytest.mark.django_db
def test_companies_partnership_add(
    client: Client,
    default_company: Company,
    add_company: Callable,
    auth_headers_admin: dict,
) -> None:
    """
    Тест partnership_add_partner компании админом
    """
    company1 = add_company(name="Компания")
    resp = client.post(
        f"/api/v1/companies/{default_company.id}/partnership/add/",
        {"id": company1.id},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["detail"] == "Сотрудничество успешно добавлено!"


@pytest.mark.django_db
def test_companies_partnership_remove(
    client: Client,
    default_company: Company,
    add_company: Callable,
    auth_headers_admin: dict,
) -> None:
    """
    Тест partnership_remove_partner компании админом
    """
    company1 = add_company(name="Компания")
    default_company.partners_companies.add(company1)
    default_company.save()
    resp = client.post(
        f"/api/v1/companies/{default_company.id}/partnership/remove/",
        {"id": company1.id},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["detail"] == "Сотрудничество успешно прекращено!"


@pytest.mark.django_db
def test_companies_offices_create(
    client: Client, default_company: Company, auth_headers_admin: dict
) -> None:
    """
    Тест create офиса админом
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
        **auth_headers_admin,
    )
    assert resp.status_code == 201
    assert resp.data["name"] == "string"
    assert resp.data["country"] == "AF"
    assert resp.data["address"] == "string"
    assert resp.data["company"] == default_company.id


@pytest.mark.django_db
def test_companies_offices_update(
    client: Client, default_office: Office, auth_headers_admin: dict
) -> None:
    """
    Тест update офиса админом
    """
    resp = client.put(
        f"/api/v1/companies/offices/{default_office.id}/",
        {"name": "string", "country": "BY", "address": "string"},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "string"
    assert resp.data["country"] == "BY"
    assert resp.data["address"] == "string"
    assert resp.data["company"] == default_office.company.id


@pytest.mark.django_db
def test_companies_offices_partial_update(
    client: Client, default_office: Office, auth_headers_admin: dict
) -> None:
    """
    Тест partial_update офиса админом
    """
    resp = client.patch(
        f"/api/v1/companies/offices/{default_office.id}/",
        {"is_active": False},
        content_type="application/json",
        **auth_headers_admin,
    )
    assert resp.status_code == 200
    assert resp.data["company"] == default_office.company.id
    assert not resp.data["is_active"]
