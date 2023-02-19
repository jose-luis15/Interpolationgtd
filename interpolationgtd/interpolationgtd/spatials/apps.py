from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "interpolationgtd.spatials"
    verbose_name = _("Spatials")

    def ready(self):
       pass