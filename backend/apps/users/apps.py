"""
Модуль конфигурации приложения Пользователи
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Класс конфигурации приложения Пользователи
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.users'
    verbose_name = 'Пользователи'
