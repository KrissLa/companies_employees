"""
Модуль с классами, проверяющими наличие прав
"""

from django.db.models.base import ModelBase
from loguru import logger
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet


class IsAdminOrAnon(BasePermission):
    """
    Доступ только администраторам и неавторизованным
    """

    def has_permission(self, request: Request, view: ViewSet) -> bool:
        return bool(not request.user or not request.user.is_authenticated
                    or request.user.is_staff)


class IsAdminOrIsSelf(BasePermission):
    """
    Доступ только администраторам или содателю записи
    """

    def has_object_permission(self, request: Request, view: ViewSet,
                              obj: ModelBase) -> bool:
        return bool(bool(obj == request.user) or request.user.is_staff)


class IsAdminOrIsOwner(BasePermission):
    """
    Доступ к созданию записи администраторам
    или создание записи с ссылкой на себя
    """

    def has_permission(self, request: Request, view: ViewSet) -> bool:
        try:
            user = request.data['user']
        except KeyError:
            user = None
        return bool(bool(user == request.user.id) or request.user.is_staff)


class IsAdminOrIsOwnerObject(BasePermission):
    """
    Доступ только администраторам или владельцу записи
    """

    def has_object_permission(self, request: Request, view: ViewSet,
                              obj: ModelBase) -> bool:
        logger.info(obj.user)
        return bool(bool(obj.user == request.user) or request.user.is_staff)
