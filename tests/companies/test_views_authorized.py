"""
Тесты views приложения companies авторизованным пользователем
"""
from typing import Callable

import pytest
from django.test.client import Client

from backend.apps.companies.models import Company, Office


@pytest.mark.django_db
def test_companies_create_authorized(client: Client, auth_headers_default: dict) -> None:
    """
    Тест create компании пользователем
    """
    resp = client.post(
        "/api/v1/companies/",
        {
            "name": "Company_name",
        },
        content_type="application/json",
        **auth_headers_default,
    )

    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_companies_update_authorized(
    client: Client, default_company: Company, auth_headers_default: dict
) -> None:
    """
    Тест update компании пользователем
    """
    resp = client.put(
        f"/api/v1/companies/{default_company.id}/",
        {
            "name": "Company_name1",
        },
        content_type="application/json",
        **auth_headers_default,
    )

    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_companies_partial_update_authorized(
    client: Client, default_company: Company, auth_headers_default: dict
) -> None:
    """
    Тест partial_update компании пользователем
    """
    resp = client.put(
        f"/api/v1/companies/{default_company.id}/",
        {"name": "Company_name112", "is_active": False},
        content_type="application/json",
        **auth_headers_default,
    )

    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_companies_partnership_add_authorized(
    client: Client,
    default_company: Company,
    add_company: Callable,
    auth_headers_default: dict,
) -> None:
    """
    Тест partnership_add_partner компании пользователем
    """
    company1 = add_company(name="Компания")
    resp = client.post(
        f"/api/v1/companies/{default_company.id}/partnership/add/",
        {"id": company1.id},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_companies_partnership_remove_authorized(
    client: Client,
    default_company: Company,
    add_company: Callable,
    auth_headers_default: dict,
) -> None:
    """
    Тест partnership_remove_partner компании пользователем
    """
    company1 = add_company(name="Компания")
    default_company.partners_companies.add(company1)
    default_company.save()
    resp = client.post(
        f"/api/v1/companies/{default_company.id}/partnership/remove/",
        {"id": company1.id},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_companies_offices_create_authorized(
    client: Client, default_company: Company, auth_headers_default: dict
) -> None:
    """
    Тест create офиса пользователем
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
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_companies_offices_update_authorized(
    client: Client, default_office: Office, auth_headers_default: dict
) -> None:
    """
    Тест update офиса пользователем
    """
    resp = client.put(
        f"/api/v1/companies/offices/{default_office.id}/",
        {"name": "string", "country": "BY", "address": "string"},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."


@pytest.mark.django_db
def test_companies_offices_partial_update_authorized(
    client: Client, default_office: Office, auth_headers_default: dict
) -> None:
    """
    Тест partial_update офиса пользователем
    """
    resp = client.patch(
        f"/api/v1/companies/offices/{default_office.id}/",
        {"is_active": False},
        content_type="application/json",
        **auth_headers_default,
    )
    assert resp.status_code == 403
    assert resp.data["detail"] == "You do not have permission to perform this action."
