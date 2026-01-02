from rest_framework import generics
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by("name")
    serializer_class = ClientSerializer

    def gwt_queryset(self):
        qs = super().get_queryset()
        status = self.request.query_params.get("status")

        if status:
            qs = qs.filter(status=status)

        return qs

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.select_related("client").order_by("-created_at")
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.select_related("client")
    serializer_class = ProjectSerializer



