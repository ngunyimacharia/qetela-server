import factory.django
from faker import Faker
from faker.providers import internet,company, profile
from django.conf import settings
from organisations.models import Position
from django.contrib.auth.models import User
from accounts.models import UserPosition
from random import randint
import random,datetime

fake = Faker()
fake.add_provider(profile)

# add admin


# generate users
def gen_users():
    User.objects.all().delete()
    positions = Position.objects.all()
    for position in positions:
        #create user. Ensure no duplicates
        f_profile = fake.simple_profile()
        while User.objects.filter(username=f_profile['username']).count():
            f_profile = fake.simple_profile()

        user = User.objects.create_user(f_profile['username'], f_profile['mail'], 'password')
        user.first_name = f_profile['name'].split(' ')[0]
        user.last_name = f_profile['name'].split(' ')[1]
        user.save()
        #add user to organisation
        position.team.level.organisation.users.add(user)
        #add user to position
        up = UserPosition(
                user = user,
                position = position,
                start= datetime.date(randint(2000, 2019), randint(1, 11), randint(1, 28))
            )
        up.save()
