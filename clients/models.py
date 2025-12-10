from django.db import models

# Create your models here.

class Client(models.Model):
    STATUS_CHOICES = [
        ("lead", "Lead"),
        ("active", "Active"),
        ("paused", "Paused"),
        ("completed", "Completed"),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="lead",
    )
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.email}"


