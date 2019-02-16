import factory.django
from faker import Faker
from faker.providers import internet,company

from .models import Organisation
from random import randint
import random

fake = Faker()
fake.add_provider(internet)
fake.add_provider(company)

def gen_organisastion(num):
    Organisation.objects.all().delete()
    for _ in range(num):
        organisation = Organisation(
            name = fake.company(),
            website = fake.url(),
            branches = bool(random.getrandbits(1)),
            cf_frequency = randint(0, 9),
        )
        organisation.save()
