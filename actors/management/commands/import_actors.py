from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome de arquivo com lista de atores em CSV'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
     
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!'))
