from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClientActionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client_actions'
    verbose_name = _("Пользовательские действия")
