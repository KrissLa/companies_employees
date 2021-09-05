"""
Модуль для кастомных фильтров приложения users
"""

from django_filters import rest_framework as filters

from backend.apps.users.models import User, Position, Skill


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


class UserFilter(CreatedUpdatedFilter):
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


class PositionFilter(CreatedUpdatedFilter):
    """
    Фильтр для модели Position
    - companies: название компании list[str] (Google, Amazon)
    - user: usernames пользователей list[str] (user1, user2)
    - is_active: удален или нет bool (true/false)
    - created_at_after: дата, после которой должность была
    добавлена date (2021-09-03T16:40:16+03:00)
    - created_at_before: дата, до которой должность была
    добавлена date (2021-09-03T16:40:16+03:00)
    - updated_at_after: дата, после которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    - updated_at_before: дата, до которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    - position: должности list[str] (Junior, Менеджер)
    """
    companies = CharInFilter(field_name='company__name',
                             lookup_expr='in')
    user = CharInFilter(field_name='user__username',
                        lookup_expr='in')
    position = CharInFilter(field_name='position',
                            lookup_expr='in')

    class Meta:
        model = Position
        fields = ('companies', 'user', 'is_active', 'created_at', 'updated_at', 'position')


class SkillFilter(CreatedUpdatedFilter):
    """
    Фильтр для модели Skill
    - user: usernames пользователей list[str] (user1, user2)
    - level_min: минимальный уровень  int (от 1 до 10)
    - level_max: максимальный уровень int (от 1 до 10)
    - skill: навыки list[str] (Python, JS)
    - is_active: удален или нет bool (true/false)
    - created_at_after: дата, после которой навык был
    добавлен date (2021-09-03T16:40:16+03:00)
    - created_at_before: дата, до которой навык был
    добавлен date (2021-09-03T16:40:16+03:00)
    - updated_at_after: дата, после которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    - updated_at_before: дата, до которой было последнее
    обновление записи date (2021-09-03T16:40:16+03:00)
    """
    user = CharInFilter(field_name='user__username',
                        lookup_expr='in')
    level = filters.RangeFilter()
    skill = CharInFilter(field_name='skill',
                         lookup_expr='in')

    class Meta:
        model = Skill
        fields = ('user', 'level', 'skill', 'is_active', 'created_at', 'updated_at')
