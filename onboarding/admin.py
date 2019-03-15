from django.contrib import admin

#import models
from .models import Session


#customize model interaction in admin section
class SessionAdmin(admin.ModelAdmin):
    pass
#add models to admin section
admin.site.register(Session,SessionAdmin)
