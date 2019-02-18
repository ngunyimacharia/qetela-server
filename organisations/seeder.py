import factory.django
from faker import Faker
from faker.providers import internet,company
from django.conf import settings

from .models import Organisation,Level,Team
from random import randint
import random, requests, os

fake = Faker()
fake.add_provider(internet)
fake.add_provider(company)

def get_rand_word(concat = ""):
    word_file = './words'
    words = open(word_file).read().splitlines()
    word = random.choice(words)
    if len(concat):
        word = word + " " + concat
    return word.title()

# generate teams
def gen_teams(organisation):
    #get levels in organisation
    levels = Level.objects.filter(organisation=organisation).order_by('number')
    # loop through levels
    for level in levels:
        if level.number == 1:
            #if top level add one team
            team = Team(name=get_rand_word(level.label),level=level,active=True)
            team.save()
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
                    team.save()

# generate levels
def gen_levels(organisation):
    labels = ['Department','Faculty','Division','Team']
    for num in range(randint(1, 7)):
        level_no = num+organisation.branches+1
        level = Level(number=level_no,label=labels[randint(0,3)],organisation=organisation)
        level.save()
    gen_teams(organisation)

# generate organisations
def gen_organisastion(num):
    Organisation.objects.all().delete()
    for _ in range(num):
        organisation = Organisation(
            name = fake.company(),
            website = fake.url(),
            branches = bool(random.getrandbits(1)),
            cf_frequency = randint(2, 14),
        )
        organisation.save()
        gen_levels(organisation)
