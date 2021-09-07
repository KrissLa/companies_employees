"""
Модуль сериализации данных приложения users
"""
from rest_framework import serializers
from rest_framework.fields import IntegerField

from backend.apps.companies.models import Company, Office
from backend.apps.users.models import User, Position


class CompanyOfficeSerializer(serializers.ModelSerializer):
    """
    Сериализация информации об офисе
    для вывода в информации о компании
    """

    class Meta:
        model = Office
        fields = ["id", "name"]


class CompanyPartnershipSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о партнерах
    для добавления или удаления связей
    сотрудничества
    """

    id = IntegerField()

    class Meta:
        model = Company
        fields = ["id"]


class CompanyPartnersSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о партнерах
    для вывода в информации о компании
    """

    class Meta:
        model = Company
        fields = ["id", "name"]


class CompanyUserSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о пользователе
    для вывода в информации о компании
    """

    class Meta:
        model = User
        fields = ["id", "username"]


class CompanyEmployeesSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о партнерах
    для вывода в информации о компании
    """

    user = CompanyUserSerializer(read_only=True)

    class Meta:
        model = Position
        fields = ["id", "user", "position"]


class CompanySerializer(serializers.ModelSerializer):
    """
    Сеаризация данных для просмотра информации
    о компании
    """

    offices = CompanyOfficeSerializer(many=True, read_only=True)
    partners_companies = CompanyPartnersSerializer(many=True, read_only=True)
    employees = CompanyEmployeesSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"


class CompanyCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Сеаризация данных для добавления компаний
    """

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "number_of_offices",
            "number_of_employees",
            "is_active",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "number_of_offices": {"read_only": True},
            "number_of_employees": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class OfficeSerializer(serializers.ModelSerializer):
    """
    Сериализация информации об офисах
    """

    company = CompanyPartnersSerializer(read_only=True)

    class Meta:
        model = Office
        fields = "__all__"


class OfficeCreateSerializer(serializers.ModelSerializer):
    """
    Сериализация информации об офисах
    """

    class Meta:
        model = Office
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class OfficeUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализация информации об офисах
    """

    class Meta:
        model = Office
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "company": {"read_only": True},
        }
