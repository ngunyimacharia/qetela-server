from django.core.management.base import BaseCommand

from organisations.seeder import gen_organisastion
from accounts.seeder import gen_users
from goals.seeder import gen_goals

class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--app', type=str, help='Select which app to seed', )

    def handle(self, *args, **options):
        if(options['app']):
            app = options['app']
            print("Seeding the " + app + " app")
            if(app == 'organisations'):
                #seed organisations
                print("======================================================")
                gen_organisastion(10)
                return
            elif(app == 'accounts'):
                #seed users
                print("======================================================")
                gen_users()
                return
            elif(app == 'goals'):
                #seed goals
                print("======================================================")
                gen_goals()
                return
        print("Seeding the entire database")
        #seed everything
        print("======================================================")
        gen_organisastion(10)
        print("======================================================")
        gen_users()
        print("======================================================")
        gen_goals()
