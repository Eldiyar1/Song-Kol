from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from tour.models import TourAdd
from common.models import BaseModel


class Comment(BaseModel):
    stars = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)],
                                        verbose_name=_("Оценка тура"))
    name = models.CharField(max_length=100, verbose_name=_("Имя"))
    text = models.TextField(verbose_name=_("Ваш отзыв"))
    is_approved = models.BooleanField(default=False, verbose_name=_("Одобрено"))
    at_moderation = models.DateTimeField(blank=True, null=True, verbose_name=_("Дата модерации"))
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name=_("Выбрать тур"))

    def __str__(self):
        return str(format_lazy(_("Комментарий: {id} Рейтинг: звезд: {stars}"), id=self.id, stars=self.stars))

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")
        db_table = 'comment_view'


class PhotoComment(BaseModel):
    photo = models.ImageField(upload_to="comment_photos", blank=True, null=True, verbose_name=_("Фото"))
    comment = models.ForeignKey(Comment, related_name="photos", on_delete=models.CASCADE,
                                verbose_name=_("Комментарий"))

    class Meta:
        verbose_name = _("Фотография комментария")
        verbose_name_plural = _("Фотографии комментариев")
        db_table = 'photo_comment'
