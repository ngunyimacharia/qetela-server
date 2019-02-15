from django.contrib import admin

#import models
from .models import Organisation

#customize model interaction in admin section
class OrganisationAdmin(admin.ModelAdmin):
    fields = ('name','website','branches','cf_frequency')

#add models to admin section
admin.site.register(Organisation,OrganisationAdmin)
