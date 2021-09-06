"""
Модуль для указания маршрутов API
"""

from rest_framework import routers
from backend.api.v1.users import views

router = routers.DefaultRouter()
router.register(r"positions", views.PositionViewSet, basename="positions")
router.register(r"skills", views.SkillViewSet, basename="skills")
router.register(r"languages", views.LanguageViewSet, basename="languages")
router.register(r"", views.UserViewSet, basename="users")

urlpatterns: list = []

urlpatterns += router.urls
