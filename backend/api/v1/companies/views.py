"""
Модуль, в котором описываются ViewSets приложения companies
"""
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from loguru import logger
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from backend.api.v1.companies import serializers
from backend.api.v1.companies.filters import CompaniesFilter
from backend.api.v1.viewsets import CreateRetrieveUpdateListPermissionViewSet
from backend.apps.companies.models import Company


class CompanyViewSet(CreateRetrieveUpdateListPermissionViewSet):
    """
    ViewSet для модели Company
    """
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompaniesFilter
    queryset = Company.objects.all().distinct()
    serializer_class = serializers.CompanyCreateUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    permission_classes_by_action = {
        'list': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny],
    }
    serializers_by_action = {
        'retrieve': serializers.CompanySerializer,
        'add_partner': serializers.CompanyPartnershipSerializer,
        'remove_partner': serializers.CompanyPartnershipSerializer,
    }

    @action(detail=True, methods=['post'], url_path='partnership/add',
            url_name='partnership_create')
    def add_partner(self, request, pk=None):
        company = get_object_or_404(Company, pk=pk)
        try:
            company.partners_companies.add(request.data['id'])
        except ValidationError:
            return Response(status=403, data={'detail': 'Вы не можете сотрудничать с собой('})
        except IntegrityError:
            return Response(status=404, data={'detail': 'Компания для сотрудничества не найдена'})
        except ValueError:
            return Response(status=400, data={'detail': 'поле id должно быть целым числом'})
        except KeyError:
            return Response(status=400, data={'detail': 'поле id - обязательное'})
        return Response(status=200, data={'detail': 'Сотрудничество успешно добавлено!'})

    @action(detail=True, methods=['post'], url_path='partnership/remove',
            url_name='partnership_remove')
    def remove_partner(self, request, pk=None):
        try:
            partner_id = int(request.data['id'])
        except ValueError:
            return Response(status=400, data={'detail': 'поле id должно быть целым числом'})
        except KeyError:
            return Response(status=400, data={'detail': 'поле id - обязательное'})
        company = get_object_or_404(Company, pk=pk)
        if partner_id not in [company["id"] for company in company.partners_companies.all().values('id')]:
            return Response(status=404, data={'detail': 'Компании не сотрудничают!'})

        company.partners_companies.remove(partner_id)

        return Response(status=200, data={'detail': 'Сотрудничество успешно прекращено!'})
