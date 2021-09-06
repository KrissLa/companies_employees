"""
Конфигурационный модуль приложения Компании
"""

from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    """
    Конфигурация приложения Компании
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.apps.companies"
    verbose_name = "Компании"

    def ready(self) -> None:
        from . import signals

        super().ready()
