import csv
import json
from pathlib import Path
from django.core.management.base import BaseCommand
from people.models import Person
from events.models import Event, EventType
from django.utils.dateparse import parse_date
from django.db import transaction

class Command(BaseCommand):
    help = 'Import life and cultural events from a CSV file into the Event model.'

    def handle(self, *args, **kwargs):
        file_path = Path('data/csv/sample_events.csv')

        if not file_path.exists():
            self.stderr.write(self.style.ERROR(f"❌ File not found: {file_path}"))
            return

        created, skipped = 0, 0

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            with transaction.atomic():
                for row in reader:
                    try:
                        person = Person.objects.get(id=row['person_id'])
                        event_type = EventType.objects.get(code=row['event_type_code'])

                        Event.objects.create(
                            id=row['id'],
                            person=person,
                            event_type=event_type,
                            date=parse_date(row['date']) if row['date'] else None,
                            location=row['location'],
                            description=row['description'],
                            metadata=json.loads(row['metadata']) if row['metadata'] else {},
                        )
                        created += 1
                    except (Person.DoesNotExist, EventType.DoesNotExist) as e:
                        self.stderr.write(self.style.WARNING(f"⚠️ Skipping row due to missing reference: {e}"))
                        skipped += 1

        self.stdout.write(self.style.SUCCESS(f"✔ Imported {created} events. Skipped {skipped} entries."))
