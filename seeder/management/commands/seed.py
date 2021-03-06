from django.core.management.base import BaseCommand

from organisations.seeder import gen_organisations
from accounts.seeder import gen_users
from goals.seeder import gen_goals
from chats.seeder import gen_chats
from onboarding.seeder import gen_onboardings
from kudos.seeder import gen_kudos

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
                gen_organisations()
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
                #seed chats
                gen_chats()
                return
            elif(app == 'onboarding'):
                #seed onboarding
                gen_onboardings()
                return
            elif(app == 'kudos'):
                #seed kudos
                gen_kudos()
                return
        print("Seeding the entire database")

        #seed organisations
        print("======================================================")
        print("Seeding the organisations app")
        print("======================================================")
        gen_organisations()

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

        #seed onboarding
        print("======================================================")
        print("Seeding the onboarding app")
        print("======================================================")
        gen_onboardings()


        #seed kudos
        print("======================================================")
        print("Seeding the kudos app")
        print("======================================================")
        gen_kudos()
