
from .models import Client, Project
from .forms import ClientForm, ProjectForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login



# Create your views here.
@login_required
def client_list(request):
    status = request.GET.get("status")

    all_clients = Client.objects.all()

    clients = all_clients.order_by("name")
    if status:
        clients = clients.filter(status=status)

    total_all = all_clients.count()
    total_filtered = clients.count()

    lead_count = all_clients.filter(status="lead").count()
    active_count = all_clients.filter(status="active").count()
    paused_count = all_clients.filter(status="paused").count()
    completed_count = all_clients.filter(status="completed").count()

    context = {
        "clients": clients,
        "status": status,
        "status_choices": Client.STATUS_CHOICES,

        "total": total_filtered,

        "total_all": total_all,

        "lead_count": lead_count,
        "active_count": active_count,
        "paused_count": paused_count,
        "completed_count": completed_count,
    }

    return render(request, "clients/client_list.html", context)

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    projects = client.projects.all().order_by("-created_at")
    context = {
        "client": client,
        "projects": projects,
    }
    return render(request, "clients/client_detail.html", context)

@login_required
def project_list(request):
    # select related
    projects = Project.objects.select_related("client").order_by("-created_at")
    return render(request, "projects/project_list.html", {"projects": projects})

@login_required
def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect("client_detail", pk=client.pk)
    else:
        form = ClientForm()

    return render(request, "clients/client_form.html", {"form": form})

@login_required
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

@login_required
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

@login_required
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

@login_required
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


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

