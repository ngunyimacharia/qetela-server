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
            progress=increase
        )
        update.save()

# generate kpis
def gen_kpis(goal):
    metrics = [
    "Sales Revenue",
    "Net Profit Margin",
    "Gross Margin",
    "MRR (Monthly Recurring Revenue)",
    "Net Promoter Score",
    "Cost of Customer Acquisition (CAC)",
    "Customer Retention Rate",
    "Marketing qualified leads (MQL)",
    "Sales-accepted leads (SAL)",
    "Sales qualified leads (SQL)",
    "Lead-to-Conversion rate",
    "Monthly visitors",
    "Met and Overdue Milestones",
    "Employee Happiness",
    "Budget variance",
    "Capability rate",
    "Change request cycle time",
    "Error rate",
    "Mean Time between failures",
    "Story points",
    "Turnaround time",
    "Capability rate",
    "Defense density",
    "Function points",
    "Mean time to recovery",
    "Time to market",
    "Experiment cycle time",
    "Time to volume",
    "New revenue rate",
    "Brand advocate score",
    "Brand recognition score",
    "Customer satisfaction rate",
    "Brand awareness rate",
    "Churn rate",
    "Customer lifetime value",
    "Share of wallet",
    "Cycle time",
    "Revenue per employee",
    "Labour productivity",
    "Takt time",
    "Attach rate",
    "Contribution margin",
    'Gross margin',
    "Quota achievement rate",
    "Sales volume",
    "Share of wallet",
    "Monthly recurring revenue",
    "Return on investment",
    "Net present value",
    "Run rate"
    ]
    change_options = [">","=","<"]
    for _ in range(2):
        kpi = Kpi(
            goal=goal,
            metric=metrics[randint(0, len(metrics) - 1)],
            change=change_options[randint(0, len(change_options) - 1)],
            target=randint(0,1000000)
        )
        kpi.save()
        gen_updates(kpi)

# generate goals
def gen_goals():
    Goal.objects.all().delete()
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
                    title=fake.sentence(),
                    description = fake.text(),
                    start = datetime.date(current_year, randint(1, 3), randint(1, 28)),
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
