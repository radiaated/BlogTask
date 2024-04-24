
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('token/', views.login, name='token_obtain_pair'),
    path('refresh/', views.DecoratedTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register, name='register'),
]