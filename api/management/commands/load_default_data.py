import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    MODELS_TO_RUN = ["propriety", "advertisement", "booking"]

    help = f'Load initial data for models: {MODELS_TO_RUN}'

    def handle(self, *args, **options):
        # The order metter for the foreign key constrains
        
        base_command = "python ./manage.py loaddata"
        for model in self.MODELS_TO_RUN:
            path = f"{model}/fixtures/initial_data.json"
            os.system(f"{base_command} {path}")
