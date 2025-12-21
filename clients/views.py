
from .models import Client, Project
from .forms import ClientForm, ProjectForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def client_list(request):
    status = request.GET.get("status", "")

    clients = Client.objects.all().order_by("name")
    if status:
        clients = clients.filter(status=status)

    context = {
        "clients": clients,
        "status": status,
        "status_choices": Client.STATUS_CHOICES,
        "total": clients.count(),
    }

    return render(request, "clients/client_list.html", context)


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

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect("client_detail", pk=client.pk)
    else:
        form = ClientForm()

    return render(request, "clients/client_form.html", {"form": form})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            # ČIA kol kas paprastai: grįžtam į projektų sąrašą
            return redirect("project_list")
    else:
        form = ProjectForm()

    return render(request, "projects/project_form.html", {"form": form})


def project_create_for_client(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            # po išsaugojimo – grįžtam į to projekto kliento puslapį
            return redirect("client_detail", pk=project.client.pk)
    else:
        # iš anksto parenkam klientą formoje
        form = ProjectForm(initial={"client": client})

    context = {
        "form": form,
        "client": client,
    }
    return render(request, "projects/project_form.html", context)


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_detail", pk=client.pk)
    else:
        form = ClientForm(instance=client)

    return render(request, "clients/client_form.html", {"form": form})


def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            # grįžtam į to projekto kliento puslapį
            return redirect("client_detail", pk=project.client.pk)
    else:
        form = ProjectForm(instance=project)

    context = {
        "form": form,
        "project": project,
    }
    return render(request, "projects/project_form.html", context)


def home(request):
    return render(request, "home.html")


