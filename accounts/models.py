import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from organisations.models import Position

# model for userposition
class UserPosition(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        'organisations.Position',
        on_delete=models.CASCADE,
    )
    start = models.DateField()
    stop = models.DateField(null=True)
    def __str__(self):
        return self.position.title + ":" + self.user.first_name + " " + self.user.last_name
