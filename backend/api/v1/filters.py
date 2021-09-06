"""
Классы фильтров
"""
from django_filters import rest_framework as filters


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CreatedUpdatedFilter(filters.FilterSet):
    """
    Базовый класс с описание фильтрации по полям
    created_at и updated_at


    - created_at_after: дата, после которой создалась
    запись date (2021-09-03T16:40:16+03:00)
    - created_at_before: дата, до которой создалась
    запись date (2021-09-03T16:40:16+03:00)
    - updated_at_after: дата, после которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    - updated_at_before: дата, до которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    """
    created_at = filters.DateTimeFromToRangeFilter()
    updated_at = filters.DateTimeFromToRangeFilter()
