from django.urls import path
from . import views

urlpatterns = [
    path("", views.client_list, name="client_list"),
    path("<int:pk>/", views.client_detail, name="client_detail"),
    path("projects/", views.project_list, name="project_list"),
    path("new/", views.client_create, name="client_create"),
    path("projects/new", views.project_create, name="project_create"),
    path("<int:client_pk>/projects/new/", views.project_create_for_client, name="project_create_for_client"),  # 👈 naujas

]

