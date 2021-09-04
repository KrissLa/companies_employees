"""
Модуль для указания маршрутов API
"""

from rest_framework import routers
from backend.api.v1.users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns: list = []

urlpatterns += router.urls
