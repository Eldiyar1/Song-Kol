import re
import requests
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, status

from tour.models import TourAdd
from tour.api.serializers import BookingGroupTourSerializer, BookingPrivateTourSerializer, TourProgramSerializer, \
    PriceDetailCreateSerializer


class BookingGroupTourService:
    @staticmethod
    def create_booking(request_data):
        try:
            name = request_data.get("name")
            contacts = request_data.get("email_or_whatsapp")
            date_id = request_data.get("date")
            tour_id = request_data.get("tour")

            if not name:
                raise serializers.ValidationError(_("Это поле не может быть пустым"))
            elif not contacts:
                raise serializers.ValidationError(_("Это поле не может быть пустым"))
            elif not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', contacts) and not re.match(r'^\+[0-9]+$', contacts):
                raise serializers.ValidationError(
                    _("Поле контакта должно быть в формате электронной почты или номера WhatsApp")
                )

            if date_id and not isinstance(date_id, int):
                date_id = int(date_id)
            if tour_id and not isinstance(tour_id, int):
                tour_id = int(tour_id)

            request_data["date"] = date_id
            request_data["tour"] = tour_id

            serializer = BookingGroupTourSerializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            bot_token = 'Ваш_токен_бота'
            chat_id = 'Ваш_идентификатор_чата'
            message = f'Бронирование группового тура\n' \
                      f'Имя клиента: {serializer.data["name"]}\n' \
                      f'Контакты: {serializer.data["email_or_whatsapp"]}\n' \
                      f'Дата брони: {str(serializer.data["date_str"])}\n' \
                      f'Тур: {str(serializer.data["tour"])}'
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
            requests.post(url)

            return {
                "message": _("Ваш запрос успешно отправлен! Менеджер свяжется с вами в ближайшее время."),
            }, status.HTTP_201_CREATED

        except serializers.ValidationError as e:
            return {
                "message": str(e),
            }, status.HTTP_400_BAD_REQUEST

        except Exception as e:
            return {
                "message": _("Ваш запрос не был успешно отправлен! Пожалуйста, попробуйте позже."),
                "error": str(e),
            }, status.HTTP_400_BAD_REQUEST


class BookingPrivateTourService:
    @staticmethod
    def create_booking(request_data):
        try:
            name = request_data.get("name")
            contacts = request_data.get("email_or_whatsapp")

            if not name:
                raise serializers.ValidationError(_("Это поле не может быть пустым"))
            elif not contacts:
                raise serializers.ValidationError(_("Это поле не может быть пустым"))
            elif not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', contacts) and not re.match(r'^\+[0-9]+$', contacts):
                raise serializers.ValidationError(
                    _("Поле контакта должно быть в формате электронной почты или номера WhatsApp"))

            serializer = BookingPrivateTourSerializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            bot_token = 'Ваш_токен_бота'
            chat_id = 'Ваш_идентификатор_чата'
            message = f'Бронирование приватного тура\n' \
                      f'Имя клиента: {serializer.data["name"]}\n' \
                      f'Контакты: {serializer.data["email_or_whatsapp"]}\n' \
                      f'Тур: {serializer.data["tour"]}\n' \
                      f'Дата брони: {str(serializer.data["date"] + "-" + str(serializer.data["date_up_to"]))}\n'
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
            requests.post(url)

            return {
                "message": _("Ваш запрос успешно отправлен! Менеджер свяжется с вами в ближайшее время."),
            }, status.HTTP_201_CREATED

        except serializers.ValidationError as e:
            return {
                "message": str(e),
            }, status.HTTP_400_BAD_REQUEST

        except Exception:
            return {
                "message": _("Ваш запрос не был успешно отправлен! Пожалуйста, попробуйте позже."),
            }, status.HTTP_400_BAD_REQUEST


class TourProgramDUService:
    @staticmethod
    def get_tour_programs_list(request):
        tour_id = request.GET.get('tour')
        if not tour_id:
            return {"message": _("Идентификатор тура обязателен")}, status.HTTP_400_BAD_REQUEST

        try:
            tour = TourAdd.objects.get(id=tour_id)
            list_1 = []
            for program in tour.tour_program.all():
                for day in program.day_list.all():
                    list_1.append(day)
            serializer = TourProgramSerializer(list_1, many=True)
            return serializer.data, status.HTTP_200_OK
        except TourAdd.DoesNotExist:
            return {"message": _("Тур не найден")}, status.HTTP_404_NOT_FOUND


class PriceDetailsService:
    @staticmethod
    def create_price_detail(request_data):
        serializer = PriceDetailCreateSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        person = serializer.validated_data['person']
        per_person = serializer.validated_data['per_person']
        in_com = per_person * person
        serializer.validated_data['in_com'] = in_com

        serializer.save()

        return {
            'id': serializer.instance.id,
            'person': person,
            'in_com': in_com,
            'per_person': per_person
        }, status.HTTP_201_CREATED
