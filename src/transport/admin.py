from django.contrib import admin
from .models import CarRental, CarSlider, CarWithDriver, CarWithoutDriver, Taxi


class CarWithDriverInline(admin.StackedInline):
    model = CarWithDriver
    extra = 1


class CarWithoutDriverInline(admin.StackedInline):
    model = CarWithoutDriver
    extra = 1


class CarSliderInline(admin.TabularInline):
    model = CarSlider
    extra = 1


@admin.register(CarRental)
class CarRentalAdmin(admin.ModelAdmin):
    inlines = [CarWithDriverInline, CarWithoutDriverInline, CarSliderInline]
    list_display = ('name_car', 'status', 'capacity', 'transmission', 'steering_wheel', 'type_of_fuel', 'type_of_drive',
                    'engine_capacity', 'power', 'configuration', 'consumption')
    ordering = ('-created_at',)


@admin.register(Taxi)
class TaxiAdmin(admin.ModelAdmin):
    list_display = ('place_of_departure', 'place_of_arrival', 'name_taxi', 'price', 'how_hours', 'map')
    ordering = ('-created_at',)
