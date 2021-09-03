from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.apps.abstract.models import BaseAbstractModel
from backend.apps.companies.models import Company


class User(AbstractUser, BaseAbstractModel):
    """ Дополняем модель пользователя """
    patronymic = models.CharField('Отчество', max_length=255, null=True)
    age = models.SmallIntegerField('Возраст', null=True)
    companies = models.ManyToManyField(Company, through='Position')

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Position(BaseAbstractModel):
    """ Модель для хранения связи людей с компаниями """
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Человек', on_delete=models.CASCADE)
    position = models.CharField('Должность', max_length=50)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f'{self.position} - {self.user.username} в {self.company.name}'


class Skill(models.Model):
    """ Модель для хранения навыков работника """
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    skill = models.CharField('Навык', max_length=50)
    level = models.PositiveSmallIntegerField('Уровень владения навыком', help_text='от 1 до 10')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return f'{self.skill} - {self.level} - {self.user.username}'


class Language(models.Model):
    """ Модель для хранения языков работника """
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=50)
    level = models.PositiveSmallIntegerField('Уровень владения языком', help_text='от 1 до 10')

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'

    def __str__(self):
        return f'{self.language} - {self.level} - {self.user.username}'



