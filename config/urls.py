"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from clients import views as client_views

from clients.api import (
    ClientListCreateAPIView,
    ClientRetrieveUpdateDestroyAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("", client_views.home, name="home"),
    path("admin/", admin.site.urls),

    # Auth
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("signup/", client_views.signup, name="signup"),
    path("accounts/logout/", client_views.logout_view, name="logout"),

    path("clients/", include("clients.urls")),

    # --- API ---
    path("api/clients/", ClientListCreateAPIView.as_view(), name="api_client_list"),
    path(
        "api/clients/<int:pk>/",
        ClientRetrieveUpdateDestroyAPIView.as_view(),
        name="api_client_detail",
    ),
    path("api/projects/", ProjectListCreateAPIView.as_view(), name="api_project_list"),
    path(
        "api/projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="api_project_detail",
    ),
]
