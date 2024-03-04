from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy

from common.constants import CATEGORY_CHOICES
from common.models import BaseModel


class BlogNews(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_("Заголовок"))
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name=_("Категория"))
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата публикации"))
    image = models.ImageField(upload_to='blog_images', verbose_name=_("Изображение"))
    content = models.TextField(verbose_name=_("Контент"))

    def __str__(self):
        return str(
            format_lazy(_("Заголовок: {title} - Категория: {category}"), title=self.title, category=self.category))

    class Meta:
        verbose_name_plural = _('Добавить посты или новости')
        verbose_name = _('Добавить пост или новость')
        db_table = 'blog_news'


class Slides(BaseModel):
    slides = models.ImageField(upload_to='slides_images', blank=False, null=False, verbose_name=_("Изображение"))
    blogs = models.ForeignKey(BlogNews, on_delete=models.CASCADE, verbose_name=_("Блог новостей"),
                              related_name="slides", blank=False, null=False)

    class Meta:
        verbose_name_plural = _('Добавить слайды')
        verbose_name = _('Добавить слайд')
        db_table = 'slides'
