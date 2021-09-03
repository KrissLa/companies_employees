from django.db import models


class BaseAbstractModel(models.Model):
    """ Абстрактный класс для добавления информации о времени создания и обновления записи,
     а также о ее активности дочерним моделям """
    is_active = models.BooleanField('Активный', default=True)
    created_at = models.DateTimeField('Время добавления', auto_now_add=True)
    updated_at = models.DateTimeField('Время последнего изменения', auto_now=True)

    class Meta:
        abstract = True
