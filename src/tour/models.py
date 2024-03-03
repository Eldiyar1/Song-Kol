from django.db import models


class TourAdd(models.Model):
    HORSE_TOUR = '1'
    WALK_TOUR = '2'
    JEEP_TOUR = '3'
    WINTER_TOUR = '4'
    TYPE_CHOICES = (
        (HORSE_TOUR, 'Конный тур'),
        (WALK_TOUR, 'Пеший тур'),
        (JEEP_TOUR, 'Джип тур'),
        (WINTER_TOUR, 'Зимний тур'),
    )
    name = models.CharField(max_length=100)
    tour_time = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    tour_program = models.ManyToManyField('TourProgram', verbose_name="Программа тура", blank=True, null=True,
                                          related_name='tour_program')
    price = models.IntegerField()
    when_is_tour = models.CharField(max_length=100)
    type = models.CharField(max_length=100, verbose_name="Тип тура", null=True, blank=False)
    description = models.TextField(verbose_name="Краткое описание", null=True, blank=True)
    image = models.ImageField(upload_to='tour_images')
    image_2 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_3 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_4 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_5 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_6 = models.ImageField(upload_to='tour_images', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Добавления туров"
        verbose_name = "Добавление тура"
        ordering = ['-when_is_tour']


class TourProgram(models.Model):
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    day_list = models.ManyToManyField('TourProgramDay', related_name="adekvatniy_name")

    class Meta:
        verbose_name_plural = "Программы туров"
        verbose_name = "Программа тура"


class TourProgramDay(models.Model):
    how_day = models.IntegerField(verbose_name="номер дня")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Программы туров"
        verbose_name = "Программа тура"
        ordering = ['-how_day']



class Location(models.Model):
    LOCATION = '1'
    FOOD = '2'
    SLEEP = '3'
    LOCATION_CHOICE = (
        (LOCATION, 'Место'),
        (FOOD, 'Питание'),
        (SLEEP, 'Ночлег'),
    )
    WALK = '1'
    HORSE = '2'
    CAR = '3'
    TRANSPORT_CHOICES = (
        (WALK, 'Пешком'),
        (HORSE, 'Лошадь'),
        (CAR, 'Машина'),
    )
    name_location = models.CharField(max_length=100, verbose_name="Локация")
    type = models.CharField(max_length=100, verbose_name="Тип локации", choices=LOCATION_CHOICE, default=LOCATION)
    description_location = models.TextField(max_length=100, verbose_name="Описание", blank=True, null=True)
    time = models.CharField(max_length=100, verbose_name="Время поездки")
    TYPE_OF_TRANSPORT = (
        ('car', 'car'),
        ('horse', 'horse'),
        ('on foot', 'on foot'),
        ('Пешком', 'Пешком'),
        ('На машине', 'На машине'),
        ('Верхом', 'Верхом'),
    )
    type_of_transport = models.CharField(max_length=100, choices=TYPE_OF_TRANSPORT, verbose_name="тип транспорта")
    tour_program = models.ForeignKey(TourProgram, related_name='locations', on_delete=models.CASCADE, blank=True,
                                     null=True)
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name="Тур")

    def __str__(self):
        return self.name_location

    class Meta:
        verbose_name_plural = "Локации"
        verbose_name = "Локация"


class Price(models.Model):
    tour = models.OneToOneField(TourAdd, on_delete=models.CASCADE, related_name="prices",
                                verbose_name="Ценовые включения")
    price_includes = models.CharField(max_length=100)
    """Что не входит в стоимость"""
    price_not_includes = models.CharField(max_length=100)

    def __str__(self):
        return self.price_includes

    class Meta:
        verbose_name_plural = "Что входит в стоимость и не входит в стоимость"
        verbose_name = "Что входит в стоимость и не входит в стоимость"


class PriceDetail(models.Model):
    person = models.IntegerField(blank=True, null=True, verbose_name="Количество человек: ")
    in_com = models.IntegerField(blank=True, null=True, verbose_name="Общая цена: ")
    per_person = models.IntegerField(blank=True, null=True, verbose_name="Цена за одного человека: ")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name="Тур", related_name="price_details")

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
    tittle = models.CharField(max_length=100, verbose_name="Заголовок")
    what_to_bring = models.CharField(max_length=1800, verbose_name="Список")
    tittle_2 = models.CharField(max_length=100, verbose_name="Заголовок 2")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    tour = models.OneToOneField(TourAdd, on_delete=models.Case, related_name="tips", verbose_name="Тур")

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name_plural = "Советы"
        verbose_name = "Совет"


class Photo(models.Model):
    image = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment',
                              verbose_name="Добавить фото(обязательно)")
    image_2 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_3 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_4 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_5 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_6 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_7 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_8 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_9 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_10 = models.ImageField(upload_to='media/static/images/tour_images/PhotoComment', blank=True, null=True,
                                 verbose_name="Добавить фото(не обязательно)")
    tour = models.OneToOneField(TourAdd, on_delete=models.CASCADE, verbose_name="Тур", related_name="photos")

    def __str__(self):
        return self.tour.name

    class Meta:
        verbose_name = "Добавить фото"
        verbose_name_plural = "Добавить фото"


class TourDates(models.Model):
    date_from = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата от: ")
    date_up_to = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата до: ")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="dates", verbose_name="Туры")

    def __str__(self) -> str:
        return f"{self.date_from} - {self.date_up_to}"

    class Meta:
        verbose_name = "Добавить дату тура"
        verbose_name_plural = "Добавить дату тура"


class BookingGroupTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Имя: ")
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name="Контакты: ")
    date = models.ForeignKey(TourDates, on_delete=models.CASCADE, related_name="group_bookings")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="group_bookings")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Бронирование группового тура"
        verbose_name_plural = "Бронирование групповых туров"


class BookingPrivateTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Имя: ")
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name="Контакты: ")
    date = models.DateTimeField(verbose_name="Дата от: ")
    date_up_to = models.DateTimeField(verbose_name="Дата до: ")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="private_bookings")

    def __str__(self):
        return self.name + self.email_or_whatsapp + f" - {self.date} - {self.date_up_to}"

    class Meta:
        verbose_name = "Бронирование приватного тура"
        verbose_name_plural = "Бронирование приватных туров"
