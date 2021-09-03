""" Настройки админ-панели """
from django.contrib import admin

from .forms import OfficeForm
from .models import Company, Office


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Класс для настройки управления Компаниями через админ-панель """
    pass


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    """ Класс для настройки управления Офисами через админ-панель """
    form = OfficeForm
