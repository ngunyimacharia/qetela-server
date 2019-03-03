from django.db import models

#model for goals
class Goal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    start = models.DateField()
    end = models.DateField(null=True)
    parent = models.ForeignKey('self', blank=True, null=True , on_delete=models.CASCADE, related_name='children')
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    team = models.ForeignKey(
        'organisations.Team',
        on_delete=models.CASCADE,
        null=True
    )
    organisation = models.ForeignKey(
        'organisations.Organisation',
        on_delete=models.CASCADE,
    )
    completed = models.DateTimeField(null=True)
    published = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

#model for goal allocations
class GoalAllocation(models.Model):
    goal = models.ForeignKey(
        'goals.Goal',
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        'organisations.Team',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    accepted = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)


#model for KPIs
class Kpi(models.Model):
    metric = models.CharField(max_length=200)
    target = models.BigIntegerField()
    current = models.BigIntegerField(default=0)
    change = models.CharField(
        max_length=1,
        choices=(
            (">","Percentage Increase"),
            ("=","Equals"),
            ("<","Percentage Decrease")
        ),
        default="=",
    )
    goal = models.ForeignKey(
        'goals.Goal',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated

    def __str__(self):
        return "KPI:" + self.goal.title

#model for kpi updates
class KpiUpdate(models.Model):
    progress = models.IntegerField()
    kpi = models.ForeignKey(
        'goals.Kpi',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True) #date record was created
    updated = models.DateTimeField(auto_now=True) #date record was updated
