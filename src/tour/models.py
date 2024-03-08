from django.db import models
from django.utils.translation import gettext_lazy as _

from common.constants import LOCATION_CHOICE, LOCATION, TYPE_OF_TRANSPORT


class Image(models.Model):
    image = models.ImageField(upload_to='tour_images')
    tour_add = models.ForeignKey('TourAdd', on_delete=models.CASCADE, related_name='tours')

    class Meta:
        verbose_name_plural = "Фотографии"
        verbose_name = "Фотографие"


class TourAdd(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Название'))
    tour_time = models.TimeField(max_length=100, verbose_name=_('Время тура'))
    number_of_people = models.IntegerField(verbose_name=_('количество человек'))
    tour_program = models.ManyToManyField('TourProgram', verbose_name=_("Программа тура"), blank=True, null=True,
                                          related_name='tour_program')
    price = models.IntegerField(verbose_name=_('Цена'))
    when_is_tour = models.DateField(max_length=100, verbose_name=_('Когда состоится тур'))
    type = models.CharField(max_length=100, verbose_name=_("Тип тура"), null=True, blank=False)
    description = models.TextField(verbose_name=_("Краткое описание"), null=True, blank=True)

    def __str__(self):
        return f"Имя: {self.name}"

    class Meta:
        verbose_name_plural = "Добавления туров"
        verbose_name = "Добавление тура"
        ordering = ['-when_is_tour']


class TourProgram(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Заголовок"))
    day_list = models.ManyToManyField('TourProgramDay', related_name="tour_program_day_lists")

    class Meta:
        verbose_name_plural = "Программы туров"
        verbose_name = "Программа тура"


class TourProgramDay(models.Model):
    how_day = models.IntegerField(verbose_name=_("номер дня"))
    title = models.CharField(max_length=100, verbose_name=_("Заголовок"))

    # tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name=_('Тур'))

    class Meta:
        verbose_name_plural = "День программы туров"
        verbose_name = "День программа тура"
        ordering = ['-how_day']


class Location(models.Model):
    name_location = models.CharField(max_length=100, verbose_name="Локация")
    type = models.CharField(max_length=100, verbose_name="Тип локации", choices=LOCATION_CHOICE, default=LOCATION)
    description_location = models.TextField(max_length=100, verbose_name="Описание", blank=True, null=True)
    time = models.TimeField(max_length=100, verbose_name="Время поездки")

    type_of_transport = models.CharField(max_length=100, choices=TYPE_OF_TRANSPORT, verbose_name="тип транспорта")
    tour_program = models.ForeignKey(TourProgram, related_name='locations', on_delete=models.CASCADE, blank=True,
                                     null=True, verbose_name=_('программа тура'))
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name="Тур", related_name='locations')

    def __str__(self):
        return f"Название местоположения: {self.name_location}"

    class Meta:
        verbose_name_plural = "Локации"
        verbose_name = "Локация"


class Price(models.Model):
    tour = models.OneToOneField(TourAdd, on_delete=models.CASCADE, related_name="prices",
                                verbose_name="Ценовые включения")
    price_includes = models.CharField(max_length=100,
                                      verbose_name=_("цена включает в себя"))
    """Что не входит в стоимость"""
    price_not_includes = models.CharField(max_length=100,
                                          verbose_name=_("в стоимость не входит"))

    def __str__(self):
        return f"Включено в цену: {self.price_includes}"

    class Meta:
        verbose_name_plural = "Что входит в стоимость и не входит в стоимость"
        verbose_name = "Что входит в стоимость и не входит в стоимость"


class PriceDetail(models.Model):
    person = models.PositiveBigIntegerField(blank=True, null=True, verbose_name=_("Количество человек: "))
    in_com = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Общая цена: "))
    per_person = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                     verbose_name=_("Цена за одного человека: "))
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="price_details", verbose_name=_("Тур"))

    def __str__(self):
        return str(self.per_person)

    def save(
            self, force_insert=False,
            force_update=False,
            using=None,
            update_fields=None
    ):
        self.in_com = self.per_person * self.person
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = "Цена: "
        verbose_name_plural = "Цены: "


class Tips(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Заголовок"))
    what_to_bring = models.CharField(max_length=1800, verbose_name=_("Список"))
    title_2 = models.CharField(max_length=100, verbose_name=_("Заголовок 2"))
    description = models.TextField(verbose_name=_("Описание"), blank=True, null=True)
    tour = models.ForeignKey(TourAdd, on_delete=models.Case, related_name="tips", verbose_name=_("Тур"))

    def __str__(self):
        return f"Название: {self.title}"

    class Meta:
        verbose_name_plural = "Советы"
        verbose_name = "Совет"


class TourDates(models.Model):
    date_from = models.DateField(max_length=100, blank=False, null=True, verbose_name=_("Дата от: "))
    date_up_to = models.DateField(max_length=100, blank=False, null=True, verbose_name=_("Дата до: "))
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="dates", verbose_name="Туры")

    def __str__(self) -> str:
        return f"Дата с: {self.date_from} до: {self.date_up_to}"

    class Meta:
        verbose_name = "Добавить дату тура"
        verbose_name_plural = "Добавить дату тура"


class BookingGroupTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name=_("Имя: "))
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name=_("Контакты: "))
    date = models.ForeignKey(TourDates, on_delete=models.CASCADE, related_name="group_bookings", verbose_name=_("Дата"))
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="group_bookings", verbose_name=_("Тур"))

    def __str__(self) -> str:
        return f"Имя: {self.name}"

    class Meta:
        verbose_name = "Бронирование группового тура"
        verbose_name_plural = "Бронирование групповых туров"


class BookingPrivateTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name=_("Имя: "))
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name=_("Контакты: "))
    date = models.DateTimeField(verbose_name=_("Дата от: "))
    date_up_to = models.DateTimeField(verbose_name=_("Дата до: "))
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="private_bookings", verbose_name=_("Тур"))

    def __str__(self):
        return (f"Имя: {self.name}, Контакт: {self.email_or_whatsapp}, Дата начала: {self.date},"
                f"Дата окончания: {self.date_up_to}")

    class Meta:
        verbose_name = _("Бронирование приватного тура")
        verbose_name_plural = _("Бронирование приватных туров")
