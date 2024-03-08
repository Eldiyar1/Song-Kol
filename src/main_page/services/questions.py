import requests
from django.utils import timezone
from main_page.api.serializers import FormQuestionSerializer
from rest_framework import status, serializers
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from core.config.helper.env_reader import env
import re


class QuestionService:
    @staticmethod
    def create_question(self, request):
        try:
            contacts = request.data.get("contact")
            if not contacts:
                raise serializers.ValidationError(_("Поле контакта не может быть пустым"))

            if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', contacts) and not re.match(r'^\+[0-9]+$', contacts):
                raise serializers.ValidationError(
                    _("Поле контакта должно быть в формате электронной почты или номера WhatsApp")
                )

            serializer = FormQuestionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            headers = self.get_success_headers(serializer.data)

            bot_token = env('BOT_TOKEN')
            chat_id = env('CHAT_ID')
            message = (f'Вопросы с главной страницы: {serializer.validated_data["question_text"]}\n'
                       f'Контакты: {serializer.validated_data["contact"]}\n'
                       f'Создано в: {timezone.now().strftime("%d.%m.%Y %H:%M:%S")}')
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
            requests.post(url)

            response_201 = {
                "message": _("Ваш запрос успешно отправлен! Менеджер свяжется с вами в ближайшее время."),
            }
            return Response(response_201, status=status.HTTP_201_CREATED, headers=headers)
        except serializers.ValidationError as e:
            response_400 = {
                "message": _("Ваш запрос не был успешно отправлен! Пожалуйста, попробуйте позже. Ошибка: {}").format(
                    str(e))
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_400 = {
                "message": _("Ваш запрос не был успешно отправлен! Пожалуйста, попробуйте позже. Ошибка: {}").format(
                    str(e))
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
