import csv
import uuid
from pathlib import Path
from django.core.management.base import BaseCommand
from people.models import Person
from django.utils.dateparse import parse_date
from django.db import transaction

class Command(BaseCommand):
    help = 'Import person records from a CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = Path('data/csv/sample_person_with_parents.csv')

        if not file_path.exists():
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write(self.style.SUCCESS(f"Reading: {file_path}"))

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            people_buffer = []

            # Pre-index to resolve parent matching after all inserts
            parent_lookup = {}

            # Step 1: Create all people without linking parents
            for row in reader:
                person = Person(
                    id=uuid.UUID(row['id']),
                    full_name=row['full_name'],
                    first_name=row['first_name'],
                    middle_name=row['middle_name'],
                    surname=row['surname'],
                    gender=row['gender'],
                    date_of_birth=parse_date(row['date_of_birth']) if row['date_of_birth'] else None,
                    date_of_death=parse_date(row['date_of_death']) if row['date_of_death'] else None,
                    place_of_origin=row['place_of_origin'],
                    clan=row['clan'],
                    subclan=row['subclan'],
                    aliases=row['aliases'],
                    cultural_notes=row['cultural_notes'],
                    biography=row['story'],
                )
                people_buffer.append((person, row['father_name'], row['mother_name']))
                parent_lookup[person.full_name.strip()] = person

            with transaction.atomic():
                for person, _, _ in people_buffer:
                    person.save()

            # Step 2: Set parent relations
            for person, father_name, mother_name in people_buffer:
                if father_name and father_name.strip() in parent_lookup:
                    person.father = parent_lookup[father_name.strip()]
                if mother_name and mother_name.strip() in parent_lookup:
                    person.mother = parent_lookup[mother_name.strip()]
                person.save()

        self.stdout.write(self.style.SUCCESS("✔ Import completed successfully."))
