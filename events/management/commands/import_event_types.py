import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from events.models import EventType

class Command(BaseCommand):
    help = 'Import predefined event types from a CSV file into the EventType model.'

    def handle(self, *args, **kwargs):
        file_path = Path('data/csv/sample_event_types.csv')

        if not file_path.exists():
            self.stderr.write(self.style.ERROR(f"❌ File not found: {file_path}"))
            return

        created, skipped = 0, 0

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                code = row['code'].strip()
                if EventType.objects.filter(code=code).exists():
                    skipped += 1
                    continue

                EventType.objects.create(
                    code=code,
                    label=row['label'].strip(),
                    category=row['category'].strip(),
                    description=row.get('description', '').strip(),
                    is_active=row.get('is_active', 'True').strip().lower() in ['true', '1', 'yes']
                )
                created += 1

        self.stdout.write(self.style.SUCCESS(f"✔ Imported {created} event types. Skipped {skipped} already existing."))
