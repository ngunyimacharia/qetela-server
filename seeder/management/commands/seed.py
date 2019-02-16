from django.core.management.base import BaseCommand

from organisations.seeder import gen_organisastion


class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        #seed organisations
        gen_organisastion(10)
