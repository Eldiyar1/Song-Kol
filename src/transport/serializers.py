from rest_framework import serializers

from .models import CarRental, CarSlider, Taxi, CarWithDriver, CarWithoutDriver


class CarWithDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWithDriver
        fields = ('per_kilometer', 'driver_comfort')


class CarWithoutDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWithoutDriver
        fields = ('how_days_driving',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSlider
        fields = ('id', 'car_slider')


class CarRentalSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False, read_only=True)
    upload_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    car_with_driver = CarWithDriverSerializer(required=False)
    car_without_driver = CarWithoutDriverSerializer(required=False)

    class Meta:
        model = CarRental
        fields = ('id', 'name_car', 'status', 'capacity', 'transmission', 'steering_wheel', 'type_of_fuel',
                  'type_of_drive', 'engine_capacity', 'power', 'configuration', 'consumption', 'photos',
                  'car_with_driver', 'car_without_driver', 'upload_images')

    def create(self, validated_data):
        car_sliders = validated_data.pop('upload_images', [])
        car_rental = CarRental.objects.create(**validated_data)
        for car_slider in car_sliders:
            CarSlider.objects.create(car_rental=car_rental, car_slider=car_slider)
        return car_rental


class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ('place_of_departure', 'place_of_arrival', 'name_taxi', 'price', 'how_hours', 'map')
