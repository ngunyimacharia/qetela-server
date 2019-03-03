from django.core.management.base import BaseCommand

from organisations.seeder import gen_organisastion
from accounts.seeder import gen_users
from goals.seeder import gen_goals
from chats.seeder import gen_chats

class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--app', type=str, help='Select which app to seed', )

    def handle(self, *args, **options):
        if(options['app']):
            app = options['app']
            print("======================================================")
            print("Seeding the " + app + " app")
            print("======================================================")
            if(app == 'organisations'):
                #seed organisations
                gen_organisastion(10)
                return
            elif(app == 'accounts'):
                #seed users
                gen_users()
                return
            elif(app == 'goals'):
                #seed goals
                gen_goals()
                return
            elif(app == 'chats'):
                #seed goals
                gen_chats()
                return
        print("Seeding the entire database")

        #seed organisations
        print("======================================================")
        print("Seeding the organisations app")
        print("======================================================")
        gen_organisastion(1)

        #seed users
        print("======================================================")
        print("Seeding the accounts app")
        print("======================================================")
        gen_users()

        #seed goals
        print("======================================================")
        print("Seeding the goals app")
        print("======================================================")
        gen_goals()

        #seed chats
        print("======================================================")
        print("Seeding the chats app")
        print("======================================================")
        gen_chats()
