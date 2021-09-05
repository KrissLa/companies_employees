"""
Модуль для указания маршрутов API
"""

from rest_framework import routers
from backend.api.v1.companies import views

router = routers.DefaultRouter()
router.register(r'', views.CompanyViewSet, basename='companies')

urlpatterns: list = []

urlpatterns += router.urls
