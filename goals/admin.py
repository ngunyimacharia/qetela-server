from django.contrib import admin

#import models
from .models import Goal, GoalAllocation

class GoalAllocationInLine(admin.TabularInline):
    model = GoalAllocation
    extra = 3

#customize model interaction in admin section
class GoalAdmin(admin.ModelAdmin):
    inlines = [GoalAllocationInLine]

#add models to admin section
admin.site.register(Goal,GoalAdmin)
