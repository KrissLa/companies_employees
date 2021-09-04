"""
Модуль, в котором описываются ViewSets приложения users
"""

from rest_framework import permissions

from backend.api.v1 import permissions as permissions_custom
from backend.api.v1.users import serializers
from backend.api.v1.viewsets import CreateRetrieveUpdateListPermissionViewSet
from backend.apps.users.models import User


class UserViewSet(CreateRetrieveUpdateListPermissionViewSet):
    """
    ViewSet для модели User
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserCreateUpdateSerializer
    permission_classes = [permissions_custom.IsAdminOrIsSelf]
    permission_classes_by_action = {
        'list': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny],
        'create': [permissions_custom.IsAdminOrAnon],
    }
    serializers_by_action = {
        'list': serializers.UserListSerializer,
        'retrieve': serializers.UserRetrieveSerializer,
    }
