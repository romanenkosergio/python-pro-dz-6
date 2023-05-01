from django.core.management.base import BaseCommand
from faker import Faker

from teachers.constants import SUBJECT_CHOICES
from teachers.models import Teacher

fake = Faker()


class Command(BaseCommand):
    help = "Generate teachers"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, help="Indicates the number of teachers to be created"
        )

    def handle(self, *args, **options):
        count = options["count"] or 100
        for i in range(count):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                subject=fake.random_element(elements=SUBJECT_CHOICES),
                birthday=fake.date_of_birth(),
            )
        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {count} teachers")
        )
