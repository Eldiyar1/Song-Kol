from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogAndNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_and_news'
    verbose_name = _("Блог и Новости")
