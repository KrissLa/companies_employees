"""
Модуль, описывающий схему базы данных
приложения users
"""

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from backend.apps.abstract.models import BaseAbstractModel
from backend.apps.companies.models import Company


class User(AbstractUser, BaseAbstractModel):
    """ Дополняем модель пользователя """
    patronymic = models.CharField('Отчество', max_length=255, blank=True, null=True)
    age = models.PositiveSmallIntegerField('Возраст', blank=True, null=True,
                                           validators=[
                                               MaxValueValidator(150),
                                               MinValueValidator(0)
                                           ]
                                           )
    companies = models.ManyToManyField(Company, through='Position', blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Position(BaseAbstractModel):
    """ Модель для хранения связи людей с компаниями """
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.CASCADE,
                                related_name='employees')
    user = models.ForeignKey(User, verbose_name='Человек', on_delete=models.CASCADE,
                             related_name='user_companies')
    position = models.CharField('Должность', max_length=50)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self) -> str:
        return f'{self.position} - {self.user.username} в {self.company.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for company in self.user.companies.all():
            company.get_number_of_employees()


class Skill(BaseAbstractModel):
    """ Модель для хранения навыков работника """
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                             related_name='skills')
    skill = models.CharField('Навык', max_length=50)
    level = models.PositiveSmallIntegerField('Уровень владения навыком',
                                             help_text='от 1 до 10',
                                             validators=[
                                                 MaxValueValidator(10),
                                                 MinValueValidator(1)
                                             ])

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self) -> str:
        return f'{self.skill} - {self.level} - {self.user.username}'


class Language(BaseAbstractModel):
    """ Модель для хранения языков работника """
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                             related_name='languages')
    language = models.CharField('Язык', max_length=50)
    level = models.PositiveSmallIntegerField('Уровень владения языком',
                                             help_text='от 1 до 10',
                                             validators=[
                                                 MaxValueValidator(10),
                                                 MinValueValidator(1)
                                             ])

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'

    def __str__(self) -> str:
        return f'{self.language} - {self.level} - {self.user.username}'
