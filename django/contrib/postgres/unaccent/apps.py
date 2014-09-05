from django.apps import AppConfig
from django.db.models import CharField, TextField
from django.utils.translation import ugettext_lazy as _

from . import lookups

class UnaccentConfig(AppConfig):
    name = 'django.contrib.postgres.unaccent'
    verbose_name = _("Unaccent")

    def ready(self):
        CharField.register_lookup(lookups.Unaccent)
        TextField.register_lookup(lookups.Unaccent)
