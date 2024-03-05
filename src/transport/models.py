from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from common.models import BaseModel

from common.constants import STATUS_CHOICES


class CarWithDriver(BaseModel):
    car = models.OneToOneField('CarRental', on_delete=models.CASCADE, related_name='car_with_driver')
    per_kilometer = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Стоимость за километр'))
    driver_comfort = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name=_('Стоимость питания и проживания водителя на 1 день'))

    class Meta:
        verbose_name = _("Машина с водителем")
        verbose_name_plural = _("Машина с водителем")

    def __str__(self):
        return self.car.name_car


class CarWithoutDriver(BaseModel):
    car = models.OneToOneField('CarRental', on_delete=models.CASCADE, related_name='car_without_driver')
    how_days_driving = models.PositiveIntegerField(verbose_name=_('Количество дней езды без водителя'))

    class Meta:
        verbose_name = _("Машина без водителя")
        verbose_name_plural = _("Машина без водителя")

    def __str__(self):
        return self.car.name_car


class CarRental(BaseModel):
    name_car = models.CharField(max_length=100, verbose_name=_('Наименование машины'))
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name=_('Статус машины'))
    capacity = models.PositiveIntegerField(verbose_name=_('Вместимость машины'))
    transmission = models.CharField(max_length=100, verbose_name=_('Коробка передач'))
    steering_wheel = models.CharField(max_length=100, verbose_name=_('Руль'))
    type_of_fuel = models.CharField(max_length=100, verbose_name=_('Тип топлива'))
    type_of_drive = models.CharField(max_length=100, verbose_name=_('Тип привода'))
    engine_capacity = models.PositiveIntegerField(verbose_name=_('Мощность двигателя'))
    power = models.CharField(max_length=100, verbose_name=_('Скорость'))
    configuration = models.CharField(max_length=100, verbose_name=_('Конфигурация машины'))
    consumption = models.CharField(max_length=100, verbose_name=_('Расход'))

    def __str__(self):
        return str(format_lazy(_('Название: {name}'), name=self.name_car))


class CarSlider(BaseModel):
    car_slider = models.ImageField(upload_to="car_slider", blank=True, null=True, verbose_name=_("Фото"))
    car_rental = models.ForeignKey(CarRental, related_name="photos", on_delete=models.CASCADE,
                                   verbose_name=_("Машина в аренду"))

    class Meta:
        verbose_name = _("Фотография машины")
        verbose_name_plural = _("Фотографии машин")
        db_table = 'car_slider'


class Taxi(BaseModel):
    place_of_departure = models.CharField(max_length=100, verbose_name=_('Место отъезда'))
    place_of_arrival = models.CharField(max_length=100, verbose_name=_('Место приема'))
    name_taxi = models.CharField(max_length=100, verbose_name=_('Тип такси'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    how_hours = models.CharField(max_length=40, verbose_name=_('Количество часов'))
    map = models.ImageField(upload_to='taxi_map_to_path', blank=True, null=True, verbose_name=_("Карта пути таксиста"))

    def __str__(self):
        return str(format_lazy(_('Место отъезда: {departure} - Место приема: {arrival} - Тип такси: {taxi}'),
                               departure=self.place_of_departure, arrival=self.place_of_arrival, taxi=self.name_taxi))

    class Meta:
        verbose_name = _("Такси")
        verbose_name_plural = _("Такси")
        db_table = 'taxi'
