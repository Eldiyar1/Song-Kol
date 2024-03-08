from rest_framework import serializers

from tour.models import (
    TourAdd,
    TourProgram,
    Price,
    Tips,
    TourDates,
    BookingPrivateTour,
    BookingGroupTour, PriceDetail,
    Location, TourProgramDay, Image
)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "image", "id",
        )
        read_only_fields = fields


class TourProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourProgram
        fields = ('title', 'day_list')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.title,
        }


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id',
            'price_includes',
            'price_not_includes',
        )


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name_location', 'type', 'description_location')


class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tips
        fields = \
            [
                "title",
                "what_to_bring",
                "title_2",
                "description"
            ]


class TourDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDates
        fields = ('date_from', "date_up_to", "tour")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class PriceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDetail
        fields = ('person', 'in_com', 'per_person', 'tour')
        read_only_fields = ('in_com',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class TourAddSerializer(serializers.ModelSerializer):
    tours = ImageSerializer(many=True, required=False, read_only=True, label='Фотографии')
    tour_program = TourProgramSerializer(many=True, label='Программа тура')
    prices = PriceSerializer(read_only=True)
    locations = LocationSerializer(many=True, read_only=True)
    tips = TipsSerializer(many=True, read_only=True)
    dates = TourDatesSerializer(many=True, read_only=True)
    price_details = PriceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = TourAdd
        fields = (
            'id', 'name', 'tour_time', 'number_of_people', 'price', 'type', 'description', 'when_is_tour', 'tours',
            'tour_program', 'prices', 'locations', 'tips', 'dates', 'price_details')


class TourProgramDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourProgramDay
        fields = ('how_day', "title", 'tour')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.title,
            'day': instance.how_day,
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        price_includes = data.get('price_includes', '')
        price_not_includes = data.get('price_not_includes', '')

        if isinstance(price_includes, str):
            data['price_includes'] = [value.strip() for value in price_includes.split(',') if value.strip()]
        else:
            del data['price_includes']  # Удалить поле, если значение не является строкой

        if isinstance(price_not_includes, str):
            data['price_not_includes'] = [value.strip() for value in price_not_includes.split(',') if value.strip()]
        else:
            del data['price_not_includes']  # Удалить поле, если значение не является строкой

        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        what_to_bring = data.get('what_to_bring', '')
        if isinstance(what_to_bring, str):
            data['what_to_bring'] = [value.strip() for value in what_to_bring.split(',') if value.strip()]
        return data


class BookingPrivateTourSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d.%m.%Y")
    date_up_to = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = BookingPrivateTour
        fields = ('id', 'name', 'email_or_whatsapp', 'date', 'date_up_to', 'tour')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class BookingGroupTourSerializer(serializers.ModelSerializer):
    date_str = serializers.SerializerMethodField(read_only=True, default='None')

    class Meta:
        model = BookingGroupTour
        fields = ('id', 'name', 'email_or_whatsapp', 'date', 'date_str', 'tour')

    def get_date_str(self, instance):
        return str(instance.date)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class PriceDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDetail
        fields = ('id', "person", "per_person", "tour", 'in_com')
        read_only_fields = ('in_com',)
