from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from clients.models import Client


class ClientAPITests(APITestCase):
    def setUp(self):

        # create several clients with different statuses
        self.client_lead = Client.objects.create(
            name="Lead One",
            email="lead@example.com",
            status="lead",
        )
        self.client_active = Client.objects.create(
            name="Active One",
            email="active@example.com",
            status="active",
        )
        self.client_paused = Client.objects.create(
            name="Paused One",
            email="paused@example.com",
            status="paused",
        )

    def test_list_returns_all_clients_without_filter(self):
        url = reverse("api_client_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_filters_by_status_active(self):
        url = reverse("api_client_list")
        response = self.client.get(url, {"status": "active"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # only one active
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["email"], "active@example.com")

    def test_list_filters_by_status_lead(self):
        url = reverse("api_client_list")
        response = self.client.get(url, {"status": "lead"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["email"], "lead@example.com")

    def test_list_with_unknown_status_returns_empty_list(self):
        url = reverse("api_client_list")
        response = self.client.get(url, {"status": "does-not-exist"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)



