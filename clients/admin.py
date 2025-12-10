from django.contrib import admin

# Register your models here.

from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "status", "country", "created_at")
    list_filter = ("status", "country")
    search_fields = ("name", "email", "company")
