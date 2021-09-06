"""
Тесты для сериализаторов приложения companies
"""
import pytest

from backend.api.v1.companies import serializers
from backend.apps.companies.models import Company


@pytest.mark.django_db
def test_company_create_update_serializer() -> None:
    valid_data = {
        'name': 'Company',
        'is_active': True
    }
    serializer = serializers.CompanyCreateUpdateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    valid_data.pop('password', None)
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_company_create_update_serializer() -> None:
    invalid_serializer_data = {
        'is_active': True
    }
    serializer = serializers.CompanyCreateUpdateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"name": ["This field is required."]}


@pytest.mark.django_db
def test_company_partnership_serializer() -> None:
    valid_data = {
        'id': 1,
    }
    serializer = serializers.CompanyPartnershipSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    valid_data.pop('password', None)
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_company_partnership_serializer() -> None:
    invalid_serializer_data: dict = {}
    serializer = serializers.CompanyPartnershipSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"id": ["This field is required."]}


@pytest.mark.django_db
def test_office_create_serializer(default_company: Company) -> None:
    valid_data = {
        'is_active': True,
        'name': 'string',
        'country': 'AF',
        'address': 'string',
        'company': default_company.id
    }
    serializer = serializers.OfficeCreateSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data.get('company') == default_company
    assert serializer.validated_data.get('address') == valid_data['address']
    assert serializer.validated_data.get('country') == valid_data.get('country')
    assert serializer.validated_data.get('name') == valid_data.get('name')
    assert serializer.validated_data.get('is_active') == valid_data.get('is_active')
    assert serializer.data == valid_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_office_create_serializer() -> None:
    invalid_serializer_data = {
        'is_active': True,
        'name': 'string',
        'country': 'AF',
        'address': 'string'
    }
    serializer = serializers.OfficeCreateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"company": ["This field is required."]}
