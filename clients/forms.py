from django import forms
from .models import Client, Project



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

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "client",
            "title",
            "description",
            "budget",
            "status",
            "start_date",
            "due_date",
        ]
        widgets = {
            "start_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }
