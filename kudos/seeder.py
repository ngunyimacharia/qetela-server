import factory.django
from faker import Faker
from faker.providers import lorem,date_time,misc

from .models import Kudo
from django.contrib.auth.models import User
from random import randint
import sys, pytz
# import random,datetime,pytz

fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)
fake.add_provider(misc)


def gen_kudos():
    Kudo.objects.all().delete()
    users = User.objects.all()
    for reciever in users:
        for _ in range(2):

            #get user to give Kudos
            count = len(users)
            random_index = randint(0, count - 1)
            sender = users[random_index]

            kudo = Kudo(
                title = fake.sentence(nb_words=randint(1,7)),
                description = fake.paragraph(),
                sender = sender,
                reciever = reciever,
            )
            kudo.save()
