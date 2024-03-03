from rest_framework import serializers

from .models import (
    CarRental,
    Taxi
)


class CarRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRental
        exclude = ['image'] + [f"image_{i}" for i in range(2, 11)]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        host = self.context.get('request').get_host() if self.context.get('request') else ''
        images = [f"{host}{instance.image.url}"]
        for i in range(2, 11):
            image_key = f'image_{i}'
            image_instance = getattr(instance, image_key)
            if image_instance:
                image_url = f"{host}{image_instance.url}"
                images.append(image_url)
        data['images'] = images
        return data


class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = '__all__'
