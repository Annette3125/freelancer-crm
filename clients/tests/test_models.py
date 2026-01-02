from django.test import TestCase
from clients.models import Client, Project


class ClientModelTests(TestCase):
    def test_str_returns_name_and_email(self):
        client = Client.objects.create(
            name="Test User",
            email="test@example.com",
        )

        self.assertEqual(str(client), "Test User test@example.com")


class ProjectModelTests(TestCase):
    def test_str_returns_title_and_client(self):
        client = Client.objects.create(
            name="Client One",
            email="client@example.com",
        )

        project = Project.objects.create(
            client=client,
            title="Data Pipeline",
            status="planned",
        )

        self.assertIn("Data Pipeline", str(project))
        self.assertIn("Client One", str(project))