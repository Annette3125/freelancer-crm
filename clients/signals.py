from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Client, Project


@receiver(post_save, sender=Project)
def update_client_status_on_project_save(sender, instance: Project, created, **kwargs):
    """
    when create / renew Project:
    - if there is active project -> client form lead became active,
    - if all projects completed -> client became completed.
    """
    client = instance.client

    # 1) if there is even one "active" project, or client still lead -> make active
    active_statuses = {"planned", "in_progress"}

    if instance.status in active_statuses and client.status == "lead":
        client.status = "active"
        client.save(update_fields=["status"])
        return

    # 2) if all client projects are completed -> make client.completed
    all_statuses = list(client.projects.values_list("status", flat=True))

    if all_statuses and all(status == "completed" for status in all_statuses):
        if client.status != "completed":
            client.status = "completed"
            client.save(update_fields=["status"])
