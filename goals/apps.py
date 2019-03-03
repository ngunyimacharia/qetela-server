from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GoalsConfig(AppConfig):
    name = 'goals'
    verbose_name = _('goals')
    def ready(self):
        import goals.signals  #import signals for app triggers
