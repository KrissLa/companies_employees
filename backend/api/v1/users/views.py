"""
Модуль, в котором описываются ViewSets приложения users
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from backend.api.v1 import permissions as permissions_custom
from backend.api.v1.users import serializers
from backend.api.v1.users.filters import UserFilter, PositionFilter
from backend.api.v1.viewsets import CreateRetrieveUpdateListPermissionViewSet
from backend.apps.users.models import User, Position


class UserViewSet(CreateRetrieveUpdateListPermissionViewSet):
    """
    ViewSet для модели User
    """
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    queryset = User.objects.all().distinct()
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


class PositionViewSet(CreateRetrieveUpdateListPermissionViewSet):
    """
    ViewSet для модели Position
    """
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PositionFilter
    queryset = Position.objects.all()
    serializer_class = serializers.PositionSerializer
    permission_classes = [permissions.IsAdminUser]
    permission_classes_by_action = {
        'list': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny],
    }
