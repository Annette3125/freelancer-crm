from django.urls import path
from . import views

urlpatterns = [
    path("", views.client_list, name="client_list"),
    path("<int:pk>/", views.client_detail, name="client_detail")

]

