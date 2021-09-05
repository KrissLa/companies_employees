"""
Модуль для описания таблиц в базе данных приложения Компании
"""

from django.db import models
from django_countries.fields import CountryField

from backend.apps.abstract.models import BaseAbstractModel


class Company(BaseAbstractModel):
    """
    Класс для создания таблицы companies_company в базе данных
    """
    name = models.CharField('Название компании', max_length=255)
    number_of_offices = models.PositiveSmallIntegerField('Количество офисов', default=0)
    number_of_employees = models.PositiveIntegerField('Количество сотрудников', default=0)
    partners_companies = models.ManyToManyField("self", verbose_name='Партнеры',
                                                related_name="partners", blank=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self) -> str:
        return f'Компания {self.name}'

    def get_number_of_offices(self):
        number = self.offices.filter(is_active=True).count()
        self.number_of_offices = number
        self.save()

    def get_number_of_employees(self):
        number = self.employees.filter(is_active=True).distinct('user').count()
        self.number_of_employees = number
        self.save()


class Office(BaseAbstractModel):
    """
    Класс для создания таблицы companies_office в базе данных
    """
    name = models.CharField('Название офиса', max_length=255)
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.CASCADE,
                                related_name='offices')
    country = CountryField(verbose_name='Страна', blank_label='(Выберите страну)')
    address = models.CharField('Адрес офиса', max_length=400)

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self) -> str:
        return f'Офис {self.name} компании {self.company.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.company.get_number_of_offices()
