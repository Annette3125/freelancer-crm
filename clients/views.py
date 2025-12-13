from django.shortcuts import render, get_object_or_404
from .models import Client, Project

# Create your views here.

def client_list(request):
    clients = Client.objects.all().order_by("name")
    return render(request, "clients/client_list.html", {"clients": clients})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    projects = client.projects.all().order_by("-created_at")
    context = {
        "client": client,
        "projects": projects,
    }
    return render(request, "clients/client_detail.html", context)

def project_list(request):
    # select related
    projects = Project.objects.select_related("client").order_by("-created_at")
    return render(request, "projects/project_list.html", {"projects": projects})


