from django.core.management.base import BaseCommand

from clients.ai import summarize_project_text
from clients.models import Project


class Command(BaseCommand):
    help = "Generate AI summaries for projects that don't have one yet."

    def handle(self, *args, **options):
        qs = Project.objects.filter(summary__exact="")  # only where summary empty

        if not qs.exists():
            self.stdout.write(self.style.WARNING("No projects without summary. Nothing to do."))
            return

        for project in qs:
            self.stdout.write(f"Processing project #{project.pk}: {project.title!r}...")

            summary = summarize_project_text(

                description=project.description or "",

                notes="",
            )

            project.summary = summary
            project.save(update_fields=["summary"])

            self.stdout.write(self.style.SUCCESS(f"  ✓ Summary saved."))

        self.stdout.write(self.style.SUCCESS("Done."))