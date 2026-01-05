from django.test import TestCase
from clients.models import Client, Project


class ClientStatusSignalsTests(TestCase):
    def test_client_changes_from_lead_to_active_when_project_planned(self):
        client = Client.objects.create(
            name="Lead User",
            email="lead@example.com",
            status="lead",
        )

        Project.objects.create(
            client=client,
            title="First project",
            status="planned",
        )

        client.refresh_from_db()
        self.assertEqual(client.status, "active")

    def test_client_becomes_completed_when_all_projects_completed(self):
        client = Client.objects.create(
            name="Multi Project Client",
            email="multi@example.com",
            status="active",
        )

        Project.objects.create(
            client=client,
            title="P1",
            status="completed",
        )
        Project.objects.create(
            client=client,
            title="P2",
            status="completed",
        )

        client.refresh_from_db()
        self.assertEqual(client.status, "completed")