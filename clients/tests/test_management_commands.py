from django.core.management import call_command
from django.test import TestCase

from clients.models import Client, Project


class GenerateProjectSummariesCommandTests(TestCase):
    def test_generate_project_summaries_fills_empty_summary(self):
        # Arrange: create a client and a project without a summary
        client = Client.objects.create(
            name="Test Client",
            email="test@example.com",
            status="active",
        )

        project = Project.objects.create(
            client=client,
            title="Test Project",
            description="This is a long description for AI summary testing. " * 5,
            status="planned",
            summary="",  # leave empty
        )

        self.assertEqual(project.summary, "")

        # Act: run the management command
        call_command("generate_project_summaries")

        # Assert: summary was generated and stored
        project.refresh_from_db()
        self.assertNotEqual(project.summary, "")
        self.assertLessEqual(len(project.summary), 280)


    def test_command_does_not_override_existing_summary(self):
        # Arrange: project already has a custom summary
        client = Client.objects.create(
            name="Existing Summary Client",
            email="existing@example.com",
            status="active",
        )

        project = Project.objects.create(
            client=client,
            title="Project with summary",
            description="Some description",
            status="planned",
            summary="Custom summary that should stay.",
        )

        # Act: run the command
        call_command("generate_project_summaries")

        # Assert: summary was not overridden
        project.refresh_from_db()
        self.assertEqual(project.summary, "Custom summary that should stay.")

