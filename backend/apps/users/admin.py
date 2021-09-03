""" Настройки админ-панели """
from django.contrib import admin

from .models import User, Position, Skill, Language


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Класс для настройки управления Пользователями
    через админ-панель
    """
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """
    Класс для настройки управления Должностями
    пользователей в компании через админ-панель
    """
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Класс для настройки управления
    Навыками пользователей через админ-панель
    """
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """ Класс для настройки управления Языками пользователей через админ-панель """
    pass
