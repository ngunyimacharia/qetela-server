import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from organisations.models import Position

#model for userposition
class UserPosition(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        'organisations.Position',
        on_delete=models.CASCADE,
    )
    start = models.DateField(auto_now_add=True) #date record was created
    stop = models.DateField()
    def __str__(self):
        return self.name
