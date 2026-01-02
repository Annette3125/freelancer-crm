from django.test import TestCase
from clients.models import Client, Project

class ClientModelTests(TestCase):
    def test_str_returns_name_and_email(self):
        client = Client.objects.create(
            name="Test User",
            emai="test@example.com",
        )

        self.assertEqual(str(client), "Test user test@example.com")


