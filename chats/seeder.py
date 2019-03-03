import factory.django
from faker import Faker
from faker.providers import lorem,date_time,misc
from django.conf import settings

from goals.models import Goal
from .models import Chat,Message
from django.contrib.auth.models import User
from random import randint
import sys
# import random,datetime,pytz
fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)
fake.add_provider(misc)

def gen_messages(chat):

    if chat.team:
        #get all users in team
        users = []
        for position in chat.team.position_set.all():
            user = (position.userposition_set.all()[0]).user
            users.append(user)
    else:
        #get all users
        users = User.objects.all()
    limit = 30
    messages = []
    while len(messages) < 30:
        #get random user
        count = len(users)
        random_index = randint(0, count - 1)
        user = users[random_index]

        #get random reply if wanted
        reply = None
        if fake.boolean and len(messages):
            count = len(messages)
            random_index = randint(0, count - 1)
            reply = messages[random_index]

        #save msssage
        message = Message(
            content = fake.paragraph(),
            user=user,
            parent=reply
        )
        message.save()
        #increment
        messages.append(message)

def gen_chats():
    Chat.objects.all()
    goals = Goal.objects.all()
    for goal in goals:
        #set team for chat
        if(goal.team):
            #team goal
            team = goal.team
        elif(goal.user):
            #user goal
            team = goal.user.userposition_set.all()[0].position.team
        else:
            #organisational goal
            team = None
        #create chat
        chat = Chat(
            title = goal.title,
            team = team,
            goal = goal
        )
        chat.save()
        #generate messages
        gen_messages(chat)
