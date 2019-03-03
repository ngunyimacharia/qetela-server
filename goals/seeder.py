import factory.django
from faker import Faker
from faker.providers import lorem,date_time
from django.conf import settings

from organisations.models import Level,Organisation,Team
from .models import Goal
from random import randint
import random,datetime,pytz
fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)

# generate positions
def gen_goals():
    print("Generating organisation goals")
    organisations = Organisation.objects.all()
    # generate for organisations
    for organisation in organisations:
        print("|=> " + organisation.name)
        for _ in range(3):
            p_goal = Goal(
                title=fake.sentence(),
                description = fake.text(),
                start = datetime.date(2019, randint(1, 3), randint(1, 28)),
                end = datetime.date(2019, randint(9, 11), randint(1, 28)),
                organisation = organisation,
                published = datetime.datetime(2019, randint(9, 11), randint(1, 28),randint(1,23),randint(1,59),randint(1,59),0,tzinfo=pytz.UTC),
            )
            p_goal.save()
        # now generate for teams in organisation cascading
        levels = Level.objects.filter(organisation=organisation).order_by('number')
        for level in levels:
            teams = level.team_set.all()
            for team in teams:
                print("     |==> "+ team.name)
                # allocate parent of goal
                if(level.number == 1):
                    parent = p_goal
                else:
                    #get parent team
                    count = team.parent.goal_set.count()
                    random_index = randint(0, count - 1)
                    parent = team.parent.goal_set.all()[random_index]

                goal = Goal(
                    title=fake.sentence(),
                    description = fake.text(),
                    start = datetime.date(2019, randint(1, 3), randint(1, 28)),
                    end = datetime.date(2019, randint(9, 11), randint(1, 28)),
                    organisation = organisation,
                    team = team,
                    parent = parent,
                    published = datetime.datetime(2019, randint(9, 11), randint(1, 28),randint(1,23),randint(1,59),randint(1,59),0,tzinfo=pytz.UTC),
                )
                goal.save()
