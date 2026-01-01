from rest_framework import serializers

from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "email",
            "company",
            "country",
            "status",
            "avatar_url",
            "github_url",
            "linkedin_url",
            "website_url",
            "notes",
            "created_at",
            "updated_at",
        ]

class ProjectSerializer(serializers.ModelSerializer):
    # to see an api as a client and as a text
    client_name = serializers.CharField(source="client.name", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "client",
            "client_name",
            "title",
            "description",
            "budget",
            "status",
            "start_date",
            "due_date",
            "created_at",
            "updated_at",
        ]