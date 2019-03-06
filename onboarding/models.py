from django.db import models

#model for onboarding kits
class Kit(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#model for onboarding kits tasks
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    kit = models.ForeignKey(
        'onboarding.Kit',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#model for onboarding sesssions
class Session(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    kit = models.ForeignKey(
        'onboarding.Kit',
        on_delete=models.CASCADE,
    )
    buddy = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True,
        related_name='session_buddy_user',
    )
    completed = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#model for onboarding session progress
class Progress(models.Model):
    session = models.ForeignKey(
        'onboarding.Session',
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        'onboarding.Task',
        on_delete=models.CASCADE,
    )
    completed = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
