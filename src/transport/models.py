from django.db import models


class CarRental(models.Model):
    image = models.ImageField(upload_to='car_rental_slider')
    image_2 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_3 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_4 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_5 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_6 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_7 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_8 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_9 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    image_10 = models.ImageField(upload_to='car_rental_slider', blank=True, null=True)
    name_car = models.CharField(max_length=100, verbose_name='Наименование машины')
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('unavailable', 'unavailable'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name='Статус машины')
    capacity = models.IntegerField(verbose_name='Вместимость машины')
    transmission = models.CharField(max_length=100, verbose_name='Коробка передач')
    steering_wheel = models.CharField(max_length=100, verbose_name='Руль')
    type_of_fuel = models.CharField(max_length=100, verbose_name='Тип топлива')
    Type_of_drive = models.CharField(max_length=100, verbose_name='Тип привода')
    engine_capacity = models.IntegerField(verbose_name='Мощность двигателя')
    power = models.CharField(max_length=100, verbose_name='Скорость')
    configuration = models.CharField(max_length=100, verbose_name='Конфигурация машины')
    consumption = models.CharField(max_length=100, verbose_name='Расход')
    """with driver"""
    per_kilometer = models.IntegerField(verbose_name='за километр')
    driver_comfort = models.IntegerField(verbose_name='Питание и проживание водителя на 1 день')
    """without driver"""
    how_days_driving = models.IntegerField(verbose_name='Количество дней езды без водителя')
    how_days_driving_without_driver = models.IntegerField(verbose_name='Количество дней езды без водителя')
    how_days_driving_without_driver_2 = models.IntegerField(verbose_name='Количество дней езды без водителя')
    how_days_driving_without_driver_3 = models.IntegerField(verbose_name='Количество дней езды без водителя')

    def __str__(self):
        return self.name_car


class Taxi(models.Model):
    place_of_departure = models.CharField(max_length=100, verbose_name='Место отъезда')
    place_of_arrival = models.CharField(max_length=100, verbose_name='Место приема')
    name_taxi = models.CharField(max_length=100, verbose_name='Тип такси')
    price = models.IntegerField(verbose_name='Цена')
    how_hours = models.CharField(max_length=40, verbose_name='Количество часов')
    map = models.ImageField(upload_to='taxi_map_to_path', blank=True, null=True, verbose_name="Карта пути таксиста")

    def __str__(self):
        return self.name_taxi
