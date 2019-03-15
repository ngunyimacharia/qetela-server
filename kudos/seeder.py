import factory.django
from faker import Faker
from faker.providers import lorem,date_time,misc

from .models import Kudo, Recommendation
from django.contrib.auth.models import User
import random,datetime,pytz,sys
import sys, pytz
# import random,datetime,pytz

fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)
fake.add_provider(misc)


def gen_kudos():

    kudo_list = ['Brilliant Presentation Naledi , Cant wait to get started on Qetela','Love love Nanesi, she is a great addition to the team!','Thanks for sharing the wellness tips , they are working wonders for me already!','Thanks for organising the office party, looking forward to the next one!','Always love borrowing your brains, your insights are great!','Thanks for the help with the Aon Project ! You are a legend','Your July monthly report was conscise and thorough exactly what we needed. Welldone','Awesome job on handling the Limited client, they have decided to stay on board with us','Well done on closing the Drakenberg Client in record time !','Coffee catch up was great, I always learn so much from you.']

    Kudo.objects.all().delete()
    users = User.objects.all()
    for reciever in users:
        for _ in range(3):

            #get user to give Kudos
            count = len(users)
            random_index = random.randint(0, count - 1)
            sender = users[random_index]

            kudo = Kudo(
                title = random.choice(kudo_list),
                description = "A detailed and clear description is really important because it lets employees know what you appreciate in their actions.",
                sender = sender,
                reciever = reciever,
            )
            kudo.save()

    #generate recommendations
    gen_recommendations()


def gen_recommendations():

    recommend_list = ['Great job with the presentation earlier perhaps you can speak slower, missed out on a few points','Thanks for joining the meeting , speak up next time would love to hear your perspective . I know you know your stuff :-)','Please double check your punctuation before sending out mails to clients, dont forget no space before the full stop!','Your client interaction skills have improved significantly, try and wait for the client to finish speaking before you recommend changes','Here is a link to an awesome resource that can help you tighten your pitch , it still needs a bit of work','A great way to handle an upset client is attentively listen to the complaints before suggesting solutions','The new process is great. Rope in @Tumelo she has worked on something similar ','Just had a look at the numbers you submitted for the Hobo Tech project , maybe extend the duration to 3 months ','Thanks for dropping the report on my desk , I think the revenue figures need to revist , pop by my desk later ','Set up some time to sit with @Loyiso , he is great with forcasting figures. He can help with your report']

    Recommendation.objects.all().delete()
    users = User.objects.all()
    for reciever in users:
        for _ in range(3):

            #get user to give Kudos
            count = len(users)
            random_index = random.randint(0, count - 1)
            sender = users[random_index]

            recommendation = Recommendation(
                title = random.choice(recommend_list),
                description = "A detailed and clear description is really important because it lets employees clearly understand your recommendation.",
                sender = sender,
                reciever = reciever,
            )
            recommendation.save()
