from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from tour.models import TourAdd


class CommentView(models.Model):
    stars = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(1, 6)], verbose_name=_("Оценка тура"))
    name = models.CharField(max_length=100, verbose_name=_("Имя"))
    text = models.TextField(verbose_name=_("Ваш отзыв"))
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name=_("Выбрать тур"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата публикации"))
    is_approved = models.BooleanField(default=False, verbose_name=_("Одобрено"))
    at_moderation = models.DateTimeField(blank=True, null=True, verbose_name=_("Дата модерации"))

    def __str__(self):
        return format_lazy(_("Комментарий: {id} Рейтинг: звезд: {stars}"), id=self.id, stars=self.stars)

    class Meta:
        verbose_name_plural = _("Комментарии")
        verbose_name = _("Комментарий")
        ordering = ["-date"]
        db_table = 'comment_view'


class PhotoComment(models.Model):
    photo = models.ImageField(upload_to="comment_photos", blank=True, null=True, verbose_name=_("Фото"))
    comment = models.ForeignKey(CommentView, related_name="photos", on_delete=models.CASCADE,
                                verbose_name=_("Комментарий"))

    def __str__(self):
        return _("Фотография к комментариям")

    class Meta:
        verbose_name_plural = _("Фотографии комментариев")
        verbose_name = _("Фотография комментария")
        db_table = 'photo_comment'
