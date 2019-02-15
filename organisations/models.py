import datetime

from django.db import models
from django.utils import timezone

#model for organisations
class Organisation(models.Model):
    name = models.CharField(max_length=200) #string field max 200
    website = models.CharField(max_length=2083) #string field max 2083. That's maximum for a website string
    branches = models.BooleanField(default=0) #whether the organisation has branches. Default is no branches
    cf_frequency = models.IntegerField(default=7) #frequency of getting feedback from employees on KPIs
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated

    def __str__(self):
        return self.name
