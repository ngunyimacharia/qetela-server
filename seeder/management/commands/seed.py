from django.core.management.base import BaseCommand

from organisations.seeder import gen_organisastion
from accounts.seeder import gen_users


class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        #seed organisations
        gen_organisastion(10)
        #seed users
        gen_users()
