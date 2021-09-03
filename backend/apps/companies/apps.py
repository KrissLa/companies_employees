from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.companies'
    verbose_name = 'Компании'

    def ready(self):
        from . import signals
        super().ready()
