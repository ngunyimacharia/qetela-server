from django.contrib import admin

#import models
from .models import Organisation,Level,Team


class LevelInLine(admin.TabularInline):
    model = Level
    extra = 3

#customize model interaction in admin section
class OrganisationAdmin(admin.ModelAdmin):
    fields = ('name','website','branches','cf_frequency')
    inlines = [LevelInLine]
    list_display = ('name','website','branches','cf_frequency','created','updated')
    list_filter = ['created','updated']
    search_fields = ['name','website']


class TeamInLine(admin.TabularInline):
    model = Team
    extra = 3

class LevelAdmin(admin.ModelAdmin):
    fields = ('label','number','organisation')
    list_display = ('label','number','organisation')
    list_filter = ['organisation','created','updated']
    inlines = [TeamInLine]
    ordering = ['number']

#add models to admin section
admin.site.register(Organisation,OrganisationAdmin)
admin.site.register(Level,LevelAdmin)
