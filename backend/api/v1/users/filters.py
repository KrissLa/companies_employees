"""
Модуль для кастомных фильтров приложения users
"""

from django_filters import rest_framework as filters

from backend.apps.users.models import User


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UserFilter(filters.FilterSet):
    """
    Фильтр для модели User
    - age_min: минимальный возраст int (1,2, etc)
    - age_max: максимальный возраст int (1,2, etc)
    - companies: название компании list[str] (Company, subcompany)
    - is_active: удален или нет bool (true/false)
    - is_staff: является пользователь администратором bool (true/false)
    - date_joined_after: дата, после которой пользователь
    зарегистрировался date (2021-09-03T16:40:16+03:00)
    - date_joined_before: дата, до которой пользователь
    зарегистрировался date (2021-09-03T16:40:16+03:00)
    - created_at_after: дата, после которой пользователь
    зарегистрировался date (2021-09-03T16:40:16+03:00)
    - created_at_before: дата, до которой пользователь
    зарегистрировался date (2021-09-03T16:40:16+03:00)
    - updated_at_after: дата, после которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    - updated_at_before: дата, до которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    - position: должности list[str] (Junior, Middle)
    - skill: навыки list[str] (python, js)
    - language: языки list[str] (английский, русский)
    """
    age = filters.RangeFilter()
    date_joined = filters.DateTimeFromToRangeFilter()
    created_at = filters.DateTimeFromToRangeFilter()
    updated_at = filters.DateTimeFromToRangeFilter()
    companies = CharInFilter(field_name='user_companies__company__name',
                             lookup_expr='in')
    position = CharInFilter(field_name='user_companies__position',
                            lookup_expr='in')
    skill = CharInFilter(field_name='skills__skill', lookup_expr='in')
    language = CharInFilter(field_name='languages__language',
                            lookup_expr='in')

    class Meta:
        model = User
        fields = ('age', 'companies', 'is_active', 'is_staff',
                  'date_joined', 'created_at', 'updated_at')
