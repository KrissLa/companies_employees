"""
Модуль для кастомных фильтров приложения companies
"""

from django_filters import rest_framework as filters

from backend.api.v1.filters import CharInFilter, CreatedUpdatedFilter
from backend.apps.companies.models import Company


class CompaniesFilter(CreatedUpdatedFilter):
    """
    Фильтр для модели Company
    - name: название компании list[str] (Company, subcompany)
    - number_of_offices_min: минимальное кол-во офисов int
    - number_of_offices_max: максимальное кол-во офисов int
    - number_of_employees_min: минимальное кол-во работников int
    - number_of_employees_max: максимальное кол-во работников int
    - partners_companies: компании-сотрудники list[str] (Google, Amazon)
    - is_active: удален или нет bool (true/false)
    - created_at_after: дата, после которой была
    добавлена компания date (2021-09-03T16:40:16+03:00)
    - created_at_before: дата, до которой была
    добавлена компания date (2021-09-03T16:40:16+03:00)
    - updated_at_after: дата, после которой была
    обновлена компания последний раз date (2021-09-03T16:40:16+03:00)
    - updated_at_before: дата, до которой была
    обновлена компания последний раз date (2021-09-03T16:40:16+03:00)
    """
    number_of_offices = filters.RangeFilter()
    number_of_employees = filters.RangeFilter()
    name = CharInFilter(field_name='name',
                        lookup_expr='in')
    partners_companies = CharInFilter(field_name='partners_companies__name',
                                      lookup_expr='in')

    class Meta:
        model = Company
        fields = ('name', 'number_of_offices', 'number_of_employees',
                  'partners_companies', 'is_active', 'created_at', 'updated_at')
