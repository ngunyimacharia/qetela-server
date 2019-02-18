from django.contrib import admin

#import models
from .models import Organisation,Level


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


#add models to admin section
admin.site.register(Organisation,OrganisationAdmin)
