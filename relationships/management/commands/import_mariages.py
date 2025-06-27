import csv
import uuid
from pathlib import Path
from django.core.management.base import BaseCommand
from relationships.models import Marriage
from people.models import Person
from django.utils.dateparse import parse_date
from django.db import transaction

class Command(BaseCommand):
    help = 'Import marriage records from a CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = Path('data/csv/sample_marriages.csv')

        if not file_path.exists():
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write(self.style.SUCCESS(f"Reading: {file_path}"))

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            with transaction.atomic():
                for row in reader:
                    try:
                        husband = Person.objects.get(id=row['husband_id'])
                        wife = Person.objects.get(id=row['wife_id'])

                        marriage = Marriage(
                            id=uuid.UUID(row['id']),
                            husband=husband,
                            wife=wife,
                            start_date=parse_date(row['start_date']) if row['start_date'] else None,
                            end_date=parse_date(row['end_date']) if row['end_date'] else None,
                            marriage_type=row['marriage_type'],
                            notes=row['notes'],
                        )
                        marriage.save()
                    except Person.DoesNotExist as e:
                        self.stderr.write(self.style.WARNING(f"Skipping entry due to missing person: {e}"))

        self.stdout.write(self.style.SUCCESS("✔ Marriage import completed successfully."))
