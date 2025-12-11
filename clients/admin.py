from django.contrib import admin

# Register your models here.

from .models import Client, Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "status", "country", "created_at")
    list_filter = ("status", "country")
    search_fields = ("name", "email", "company")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "status", "budget", "start_date", "due_date")
    list_filter = ("status", "client")
    search_fields = ("title", "client__name")
