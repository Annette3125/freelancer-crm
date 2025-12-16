from django import forms
from .models import Client



class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields =[
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
        ]