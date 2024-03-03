from django.apps import AppConfig


class BlogAndNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_and_news'
    verbose_name = "Блог и Новости"
