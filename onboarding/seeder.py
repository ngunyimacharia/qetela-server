import factory.django
from faker import Faker
from faker.providers import lorem,date_time,misc

from .models import Kit,Task,Session,Progress
from django.contrib.auth.models import User
from random import randint
import sys, pytz
# import random,datetime,pytz

fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)
fake.add_provider(misc)


def gen_progress(session):
    # get completion status
    for task in session.kit.task_set.all():
        if fake.boolean(20):
            progress = Progress(
                session=session,
                task = task
            )
            progress.save()


def gen_sessions(kit):
    for _ in range(randint(10,30)):
        users = User.objects.all()
        count = len(users)
        random_index = randint(0, count - 1)
        user = users[random_index]
        random_index = randint(0, count - 1)
        buddy = users[random_index]
        completed = None
        session = Session(
            user = user,
            kit = kit,
            buddy = buddy,
            completed = completed
        )
        session.save()
        gen_progress(session)

def gen_tasks(kit):
    for _ in range(randint(3,5)):
        task = Task(
            name = fake.sentence(),
            description = fake.paragraph(),
            kit = kit
        )
        task.save()

def gen_onboardings():
    Kit.objects.all().delete()
    for _ in range(5):
        kit = Kit(
            title = fake.sentence(nb_words=randint(5,10))
        )
        kit.save()
        # generate tasks
        gen_tasks(kit)
        # generate sesssions
        gen_sessions(kit)
