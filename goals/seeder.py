import factory.django
from faker import Faker
from faker.providers import lorem,date_time
from django.conf import settings

from organisations.models import Level,Organisation,Team
from .models import Goal,Kpi,GoalAllocation,KpiUpdate
from random import randint
import random,datetime,pytz,sys
fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)


# generate kpi updates
def gen_updates(kpi):
    #set start date and end date
    start = kpi.goal.start
    today = datetime.date.today()
    if kpi.goal.end < today:
        end = kpi.goal.end
    else:
        end = today
    #variable to hold current date and current total
    current = start
    total = 0
    target = kpi.target
    while current < end and total < target:
        #update current to random update date between start and 14 days
        next_limit = current + datetime.timedelta(days=14)
        current = fake.date_time_between_dates(current,next_limit).date()
        increase = randint(0, kpi.target // 12)
        total += increase
        if total > target:
            excess_increase = total - target
            total -= increase
            increase -= excess_increase
            total += increase
        update = KpiUpdate(
            kpi=kpi,
            progress=increase,
            created = fake.past_datetime(-50,pytz.UTC)
        )
        update.save()

# generate kpis
def gen_kpis(goal):
    kpi_list = [
        {'metric':'Website Traffic Monthly','change':'=','target':100},
        {'metric':'Net Promoter Score (%)','change':'=','target':70},
        {'metric':'Traffic to Lead Ratio (%)','change':'=','target':15},
        {'metric':'Viral Coefficient (%)','change':'=','target':20},
        {'metric':'Mentions','change':'>','target':500},
        {'metric':'Monthly blog visits','change':'>','target':200},
        {'metric':'Weekly Content created','change':'=','target':40},
        {'metric':'Weekly Content created','change':'=','target':80},
    ]
    for _ in range(2):
        kpi_choice = random.choice(kpi_list)
        kpi = Kpi(
            goal=goal,
            metric=kpi_choice['metric'],
            change=kpi_choice['change'] ,
            target=kpi_choice['target'] ,
        )
        kpi.save()
        gen_updates(kpi)

# generate goals
def gen_goals():
    Goal.objects.all().delete()
    goals_list = ['Increase Quarter 1 conversion Rate by 10%','Boost Brand Awareness','Increase content Engagement ','Increase Revenue per employee by 5%','Reduce Turnover Rate of High Performers to 1 employee']
    for prev in range(2): # how many previous years to generate
        current_year = current_year=datetime.datetime.now().year - prev
        print("Generating organisation goals: "+ str(current_year))
        organisations = Organisation.objects.all()
        # generate for organisations
        for organisation in organisations:
            print("|=> " + organisation.name)
            org_goals = []
            for _ in range(3):
                # generate parent goals
                goal = Goal(
                    title=random.choice(goals_list),
                    description = "A detailed and clear goal description is really important because it lets employees know what you want done for your goal so that you're both on the same page from the start. It also means that employees can come prepared with the correct equipment and materials for the job, ready to complete your job without any delays.",#fake.text(),
                    start = datetime.date(current_year, randint(1, 2), randint(1, 28)),
                    end = datetime.date(current_year, randint(9, 11), randint(1, 28)),
                    organisation = organisation,
                    published = datetime.datetime(current_year, randint(9, 11), randint(1, 28),randint(1,23),randint(1,59),randint(1,59),0,tzinfo=pytz.UTC),
                )
                goal.save()
                org_goals.append(goal)
                gen_kpis(goal)
            # now generate for teams in organisation cascading
            levels = Level.objects.filter(organisation=organisation).order_by('number')
            for level in levels:
                teams = level.team_set.all()
                for team in teams:
                    # allocate parent of goal
                    if(level.number == 1):
                        #get parent goal
                        count = len(org_goals)
                        random_index = randint(0, count - 1)
                        parent = org_goals[random_index]
                    else:
                        #get parent team
                        p_goals = team.parent.goal_set.filter(start__year=current_year).all()
                        count = len(p_goals)
                        random_index = randint(0, count - 1)
                        parent = p_goals[random_index]

                    #save allocation
                    allocation = GoalAllocation(
                        goal=parent,
                        team=team,
                        accepted=parent.published
                    )
                    allocation.save()


                    goal = Goal(
                        title=fake.sentence(),
                        description = fake.text(),
                        start = datetime.date(current_year, randint(1, 3), randint(1, 28)),
                        end = datetime.date(current_year, randint(9, 11), randint(1, 28)),
                        organisation = organisation,
                        team = team,
                        parent = parent,
                        published = datetime.datetime(current_year, randint(9, 11), randint(1, 28),randint(1,23),randint(1,59),randint(1,59),0,tzinfo=pytz.UTC),
                    )
                    goal.save()
                    gen_kpis(goal)

                    #generate goals for individuals
                    for position in team.position_set.all():
                        user = (position.userposition_set.all()[0]).user
                        #get parent goals
                        p_goals = team.goal_set.filter(start__year=current_year).all()
                        count = len(p_goals)
                        random_index = randint(0, count - 1)
                        parent = p_goals[random_index]

                        #save allocation
                        allocation = GoalAllocation(
                            goal=parent,
                            user=user,
                            accepted=parent.published
                        )
                        allocation.save()

                        #set goal
                        goal = Goal(
                            title=fake.sentence(),
                            description = fake.text(),
                            start = datetime.date(current_year, randint(1, 3), randint(1, 28)),
                            end = datetime.date(current_year, randint(9, 11), randint(1, 28)),
                            organisation = organisation,
                            user = user,
                            parent = parent,
                            published = datetime.datetime(current_year, randint(9, 11), randint(1, 28),randint(1,23),randint(1,59),randint(1,59),0,tzinfo=pytz.UTC),
                        )
                        goal.save()
                        gen_kpis(goal)
