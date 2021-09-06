"""
Модуль, в котором описываются ViewSets приложения users
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from backend.api.v1 import permissions as permissions_custom
from backend.api.v1.users import serializers
from backend.api.v1.users.filters import (
    UserFilter,
    PositionFilter,
    SkillFilter,
    LanguageFilter,
)
from backend.api.v1.viewsets import CreateRetrieveUpdateListPermissionViewSet
from backend.apps.users.models import User, Position, Skill, Language


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
        "list": [permissions.AllowAny],
        "retrieve": [permissions.AllowAny],
        "create": [permissions_custom.IsAdminOrAnon],
    }
    serializers_by_action = {
        "list": serializers.UserListSerializer,
        "retrieve": serializers.UserRetrieveSerializer,
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
        "list": [permissions.AllowAny],
        "retrieve": [permissions.AllowAny],
    }
    serializers_by_action = {
        "create": serializers.PositionCreateSerializer,
        "update": serializers.PositionUpdateSerializer,
        "partial_update": serializers.PositionUpdateSerializer,
    }


class SkillViewSet(CreateRetrieveUpdateListPermissionViewSet):
    """
    ViewSet для модели SKill
    """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = SkillFilter
    queryset = Skill.objects.all()
    serializer_class = serializers.SkillUpdateSerializer
    permission_classes = [permissions.AllowAny]
    permission_classes_by_action = {
        "create": [permissions_custom.IsAdminOrIsOwner],
        "update": [permissions_custom.IsAdminOrIsOwnerObject],
        "partial_update": [permissions_custom.IsAdminOrIsOwnerObject],
    }
    serializers_by_action = {
        "create": serializers.SkillCreateSerializer,
        "list": serializers.SkillSerializer,
        "retrieve": serializers.SkillSerializer,
    }


class LanguageViewSet(CreateRetrieveUpdateListPermissionViewSet):
    """
    ViewSet для модели Language
    """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = LanguageFilter
    queryset = Language.objects.all()
    serializer_class = serializers.LanguageUpdateSerializer
    permission_classes = [permissions.AllowAny]
    permission_classes_by_action = {
        "create": [permissions_custom.IsAdminOrIsOwner],
        "update": [permissions_custom.IsAdminOrIsOwnerObject],
        "partial_update": [permissions_custom.IsAdminOrIsOwnerObject],
    }
    serializers_by_action = {
        "create": serializers.LanguageCreateSerializer,
        "list": serializers.LanguageSerializer,
        "retrieve": serializers.LanguageSerializer,
    }
