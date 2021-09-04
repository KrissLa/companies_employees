"""
Модуль с кастомными ViewSets
"""

from rest_framework import mixins, viewsets
from rest_framework.serializers import Serializer


class PermissionSerializerByActionMixinCustom:
    """
    Класс, который позваоляет разграничить permissions
    и serializers в зависимости от метода запроса
    """
    action: str
    permission_classes: list
    serializer_class: Serializer = None
    serializers_by_action: dict = {}
    permission_classes_by_action: dict = {}

    def get_permissions(self) -> list:
        """
        в зависимости от метода запроса выдаем список permissions
        пример:
        permission_classes_by_action = {
                'get': [AllowAny],
                'post': [IsAuthenticated],
            }
        Для неуказанных методов используются permission_classes
        """
        try:
            return [permission() for permission
                    in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self) -> Serializer:
        """
        в зависимости от метода запроса выбираем serializer
        пример:
        serializers_by_action = {
                'list':    serializers.First,
                'detail':  serializers.Second,
                # etc.
            }
        """
        return self.serializers_by_action.get(self.action,
                                              self.serializer_class)


class CreateRetrieveUpdateListPermissionViewSet(mixins.CreateModelMixin,
                                                mixins.RetrieveModelMixin,
                                                mixins.UpdateModelMixin,
                                                mixins.ListModelMixin,
                                                PermissionSerializerByActionMixinCustom,
                                                viewsets.GenericViewSet):
    """
    Viewset, который предоставляет методы `create()`, `retrieve()`, `update()`,
    `partial_update()`, `list()` и позволяет разграничить доступ к ним.
    """
    pass
