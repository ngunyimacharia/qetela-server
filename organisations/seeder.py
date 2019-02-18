import factory.django
from faker import Faker
from faker.providers import internet,company

from .models import Organisation,Level
from random import randint
import random

fake = Faker()
fake.add_provider(internet)
fake.add_provider(company)

# generate levels
def gen_levels():
    labels = ['Department','Faculty','Division','Team']
    organisations = Organisation.objects.all()
    for organisation in organisations:
        for num in range(randint(1, 7)):
            level_no = num+organisation.branches+1
            level = Level(number=level_no,label=labels[randint(0,3)],organisation=organisation)
            level.save()

# generate organisations
def gen_organisastion(num):
    Organisation.objects.all().delete()
    Level.objects.all().delete()
    for _ in range(num):
        organisation = Organisation(
            name = fake.company(),
            website = fake.url(),
            branches = bool(random.getrandbits(1)),
            cf_frequency = randint(2, 14),
        )
        organisation.save()

    gen_levels()
