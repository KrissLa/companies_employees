"""
Модуль для указания маршрутов API
"""
from django.urls import path, include

urlpatterns = [
    path('users/', include('backend.api.v1.users.routes')),
    path('companies/', include('backend.api.v1.companies.routes')),
]
