from rest_framework import serializers

from .models import (
    TourAdd,
    TourProgram,
    Price,
    Tips,
    Photo,
    TourDates,
    BookingPrivateTour,
    BookingGroupTour, PriceDetail,
    Location, TourProgramDay
)


class TourAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourAdd
        fields = (
            'id', 'name', 'tour_time', 'number_of_people', 'price', 'type', 'description', 'when_is_tour',
            'tour_program'
        )

    def to_representation(self, instance):
        host = self.context.get('request').get_host() if self.context.get('request') else ''
        data = super().to_representation(instance)
        images = [f"{host}{instance.image.url}"]
        for i in range(3, 7):
            image_key = f'image_{i}'
            image_instance = getattr(instance, image_key)
            if image_instance:
                image_url = f"{host}{image_instance.url}"
                images.append(image_url)
        data['images'] = images
        return data


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name_location', 'type', 'description_location']


class TourProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourProgram
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.title,
        }


class TourProgramDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourProgramDay
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.title,
            'day': instance.how_day,
        }
from rest_framework import serializers

from .models import FormQuestion, OurTeam, QuestionList


class FormQuestionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%d-%m-%Y')

    class Meta:
        model = FormQuestion
        fields = '__all__'


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionList
        fields = '__all__'





class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id',
            'price_includes',
            'price_not_includes',
        )

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


class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tips
        fields = \
            [
                "tittle",
                "what_to_bring",
                "tittle_2",
                "description"
            ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        what_to_bring = data.get('what_to_bring', '')
        if isinstance(what_to_bring, str):
            data['what_to_bring'] = [value.strip() for value in what_to_bring.split(',') if value.strip()]
        return data


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "TourPhoto"
        model = Photo
        fields = 'id'.split()

    def to_representation(self, instance):
        host = self.context.get('request').get_host() if self.context.get('request') else ''
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        images = [f"{host}{instance.image.url}"]
        for i in range(2, 11):
            image_key = f'image_{i}'
            image_instance = getattr(instance, image_key)
            if image_instance:
                image_url = f"{host}{image_instance.url}"
                images.append(image_url)
        data['images'] = images
        return data


class TourDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDates
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class BookingPrivateTourSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d.%m.%Y")
    date_up_to = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = BookingPrivateTour
        fields = 'id name email_or_whatsapp date date_up_to tour'.split()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class BookingGroupTourSerializer(serializers.ModelSerializer):
    date_str = serializers.SerializerMethodField(read_only=True, default='None')

    class Meta:
        model = BookingGroupTour
        fields = 'id name email_or_whatsapp date date_str tour'.split()

    def get_date_str(self, instance):
        return str(instance.date)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data

    # def validate_email_or_whatsapp(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Поле name не может быть пустым")
    #
    #         # Проверяем, что значение содержит только буквы
    #     if not re.match(r'^[a-zA-Z]+$', value):
    #         raise serializers.ValidationError("Поле name должно содержать только буквы")
    #
    #     return value


class PriceDetailCreateSerializer(serializers.ModelSerializer):
    in_com = serializers.IntegerField(read_only=True)

    class Meta:
        model = PriceDetail
        fields = 'id person per_person tour'.split()


class PriceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDetail
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tour'] = instance.tour.name
        return data


class TourDetailSerializer(serializers.ModelSerializer):
    tour_program = TourProgramSerializer(read_only=True, many=True)
    prices = PriceSerializer(read_only=True)
    price_details = PriceDetailSerializer(many=True, read_only=True)
    tips = TipsSerializer(read_only=True)
    photos = PhotoSerializer(read_only=True)
    tour_dates = TourDatesSerializer(many=True, read_only=True)

    class Meta:
        model = TourAdd
        fields = (
            'id', 'name', 'tour_time', 'number_of_people', 'price', 'when_is_tour', 'tour_program', 'prices',
            'price_details', 'tips', 'photos', 'tour_dates')

    def to_representation(self, instance):
        request = self.context.get('request')
        host = request.get_host() if request else ''
        context = self.context
        photos_serializer = self.fields['photos']
        photos_serializer.context.update(context)
        data = super().to_representation(instance)
        images = [f"{host}{instance.image.url}"]
        for i in range(2, 7):
            image_key = f'image_{i}'
            image_instance = getattr(instance, image_key)
            if image_instance:
                image_url = f"{host}{image_instance.url}"
                images.append(image_url)
        data['images'] = images
        return data
