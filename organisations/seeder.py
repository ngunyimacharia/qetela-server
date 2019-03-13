import factory.django
from faker import Faker
from faker.providers import internet,company, profile
from django.conf import settings

from .models import Organisation,Level,Team,Position
from random import randint
import random, os

fake = Faker()
fake.add_provider(internet)
fake.add_provider(company)
fake.add_provider(profile)

def get_rand_word(concat = ""):
    word_file = './words'
    words = open(word_file).read().splitlines()
    word = random.choice(words)
    if len(concat):
        word = word + " " + concat
    return word.title()

# generate positions
def gen_positions(team):
    description = "Responsible for administering & maintaining all systems on a senior level, in order to ensure internal & external customer satisfaction, and compliance to the relevant service level agreements. Responsible for the design, documentation and implementation of improvements to current systems, additional functionalities and new products. Responsible for the co-ordination of on-the-job skills transfer to technical resources in team. This position could also include the management of a team."
    jobs = ['Inbound Sales Associate','Outbound Sales Associate','Content Developer','Social Media Manager','UX & UI Designer ','Product Designer ','Software Developer','Software Engineer','Product Manager ','Data Infrastructure Engineer','Data Analyst','Recruitment Manager','Internal Recruiter','Office Manager ','Accounting Manager ','Cost Accountant','On-boarding Lead','Customer Engagement Analyst','Supply Chain Manager ','Supply Chain Analyst','Vice President Sales ','Key Accounts Manager ','Lead Generation Specialist','Finance Manager','VP Finance']
    for _ in range(5):
        position = Position(
            title=random.choice(jobs),
            team=team,
            description=description,
        )
        position.save()

# generate teams
def gen_teams(organisation):
    #print("Generating teams")
    #get levels in organisation
    levels = Level.objects.filter(organisation=organisation).order_by('number')
    # loop through levels
    for level in levels:
        if level.number == 1:
            #if top level add one team
            team = Team(name=get_rand_word(level.label),level=level,active=True)
            #print("Team:"+team.name)
            team.save()
            gen_positions(team)
        else:
            #if not top level,
            #get parent level
            p_level = Level.objects.get(organisation=organisation,number=(level.number-1))
            # get team at that level that has less than two children
            p_teams = p_level.team_set.all()
            for p_team in p_teams:
                # loop no of times needed per parent team
                for _ in range(2):
                    team = Team(name=get_rand_word(level.label),level=level,active=True,parent=p_team)
                    #print("Team:"+team.name)
                    team.save()
                    gen_positions(team)

# generate levels
def gen_levels(organisation):
    #print("Generating levels")
    labels = ['Division','Department','Team','Workgroup']
    for num in range(4):
        level_no = num+organisation.branches+1
        level = Level(number=level_no,label=labels[num],organisation=organisation)
        level.save()
        #print("Level:"+level.label)
    gen_teams(organisation)

# generate organisations
def gen_organisations(num=1):
    #print("Generating organisations")
    Organisation.objects.all().delete()
    for _ in range(num):
        organisation = Organisation(
            name = 'Pule Tech',#fake.company(),
            website = 'https://puletech.co.za',#fake.url(),
            branches = bool(random.getrandbits(1)),
            cf_frequency = randint(2, 14),
        )
        #print("Organisation:"+organisation.name)
        organisation.save()
        gen_levels(organisation)
