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

kit_list = [
    {
        'name':'Pule Tech New Joiners Kit',
        'tasks':['Complete The Strengths Finder Test ','Join Pule Tech Slack Team','Join Pule Tech Honey ','Onboarding with Marketing Team ']
    },
    {
        'name':'Marketing Department Kit',
        'tasks':['Join Marketing slack channels','Pule Tech Marketing Report 2019','Set Meeting with VP Marketing']
    }
]

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

def gen_tasks(kit,tasks):
    for task_title in tasks:
        task = Task(
            name = task_title,#fake.sentence(),
            description = "A detailed and clear task description is really important because it lets employees know what you want done for your task so that you're both on the same page from the start. It also means that employees can come prepared with the correct equipment and materials for the job, ready to complete your job without any delays.",#fake.paragraph(),
            kit = kit,
        )
        task.save()

def gen_onboardings():
    Kit.objects.all().delete()
    Task.objects.all().delete()
    Session.objects.all().delete()
    Progress.objects.all().delete()
    for kit_choice in kit_list:
        kit = Kit(
            title = kit_choice['name'] #fake.sentence(nb_words=randint(5,10))
        )
        kit.save()
        # generate tasks
        gen_tasks(kit,kit_choice['tasks'])
        # generate sesssions
        gen_sessions(kit)
