import factory.django
from faker import Faker
from faker.providers import lorem,date_time,misc
from django.conf import settings

from goals.models import Goal
from .models import Chat,Message
from django.contrib.auth.models import User
import random
import sys
# import random,datetime,pytz
fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)
fake.add_provider(misc)

def gen_messages(chat):

    message_list = ['I need some extra hands on deck to help with the calls if we are to reach the target by month end ','Super interested in this client can I jump in on the project ?','waiting on the marketing team to send projections before we can release budget ','Major delays on the due to changes in the clients schedule','Well done team enjoyed smashing this KPI with you !','Almost there team , I need help with the final presentation due Tuesday.','Anyone great with excel? , I am stuck with some calculations ','Deadline has been shifted to next Wednesday , 2 more days to make history!','I have attached the relevent background documents here','We are ahead of schedule , well done!']

    if chat.team:
        #get all users in team
        users = []
        for position in chat.team.position_set.all():
            user = (position.userposition_set.all()[0]).user
            users.append(user)
    else:
        #get all users
        users = User.objects.all()
    limit = 5
    messages = []
    while len(messages) < 5:
        #get random user
        count = len(users)
        random_index = random.randint(0, count - 1)
        user = users[random_index]

        #get random reply if wanted
        reply = None
        if fake.boolean and len(messages):
            count = len(messages)
            random_index = random.randint(0, count - 1)
            reply = messages[random_index]

        #save msssage
        message = Message(
            chat=chat,
            content = random.choice(message_list),
            user=user,
            parent=reply
        )
        message.save()
        #increment
        messages.append(message)

def gen_chats():
    Chat.objects.all().delete()
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
