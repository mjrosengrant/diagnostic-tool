"""Management command to import symptom and conditions data."""
import csv

from django.core.management.base import BaseCommand
from api.models import Condition, Symptom


class Command(BaseCommand):
    """Management command to import data from symptoms.csv."""
    help = 'Import symptoms and conditions from provided csv file.'

    def handle(self, *args, **options):
        """Execute command."""
        with open('api/symptoms.csv', 'rb') as csvfile:
            symptom_reader = csv.reader(csvfile, delimiter=',')
            for row in symptom_reader:
                # Create a Symptom from first column, and affiliated
                # Conditions for each other column in row.
                symptom_name = row[0]
                condition_names = row[1:]
                symptom, created = Symptom.objects.get_or_create(name=symptom_name)
                for name in condition_names:
                    condition, created = Condition.objects.get_or_create(name=name)
                    condition.symptoms.add(symptom)
