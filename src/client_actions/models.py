from django.db import models

from tour.models import TourAdd

STAR_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),

]


class CommentView(models.Model):
    stars = models.IntegerField(default=0, choices=STAR_CHOICES, verbose_name="Оценка тура")
    name = models.CharField(max_length=100)
    text = models.TextField(verbose_name="ваш отзыв")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name="выбрать тур")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_approved = models.BooleanField(default=False)
    at_moderation = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")

    def __str__(self):
        return f"Комментарий: {self.id} Рейтинг: звезд: {self.stars}"

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'

        ordering = ['-date']


class PhotoComment(models.Model):
    photo = models.ImageField(upload_to='comment_photos', verbose_name="фото", blank=True, null=True)
    comment = models.ForeignKey(CommentView, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return "Фотография к комментариям"

    class Meta:
        verbose_name_plural = 'Фотографии комментарии'
        verbose_name = 'Фотография комментария'
