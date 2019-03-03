from .models import KpiUpdate
from django.db.models.signals import post_save
from django.dispatch import receiver
import sys
@receiver(post_save, sender=KpiUpdate)
def update_kpi_progress(sender, instance, created, **kwargs):
    #get all updates
    kpi = instance.kpi
    updates = kpi.kpiupdate_set.all()
    for update in updates:
        #add progress
        kpi.current += update.progress

    #save
    kpi.save()
