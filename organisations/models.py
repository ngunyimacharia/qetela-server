import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#model for organisations
class Organisation(models.Model):
    name = models.CharField(max_length=200) #string field max 200
    website = models.CharField(max_length=2083,blank=True,null=True) #string field max 2083. That's maximum for a website string
    branches = models.BooleanField(default=0) #whether the organisation has branches. Default is no branches
    cf_frequency = models.IntegerField(default=7) #frequency of getting feedback from employees on KPIs
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

#model for levels
class Level(models.Model):
    number = models.IntegerField()
    label = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated
    organisation = models.ForeignKey(
        'Organisation',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.organisation.name + ":" + self.label

#model for teams
class Team(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=1)
    parent = models.ForeignKey('self', blank=True, null=True , on_delete=models.CASCADE, related_name='children')
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated
    level = models.ForeignKey(
            'Level',
            on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.level.organisation.name + ":" + self.name

#model for positions
class Position(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated
    team = models.ForeignKey(
            'Team',
            on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

#add branches to organisations
def create_branches(instance, created, raw, **kwargs):
    # Ignore fixtures and saves for existing courses.
    if not created or raw:
        return

    if instance.branches:
        Level.objects.get_or_create(number=1,label="Branch",organisation=instance)

models.signals.post_save.connect(create_branches, sender=Organisation, dispatch_uid='create_branches')
