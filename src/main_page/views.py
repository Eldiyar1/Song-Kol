import requests
from rest_framework import status, generics
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from common.decorators import limit_rate
from core.config.helper.env_reader import env
from .models import FormQuestion, OurTeam, QuestionList
from .serializers import FormQuestionSerializer, OurTeamSerializer, QuestionListSerializer


class FormQuestionCreateView(generics.CreateAPIView):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

    @limit_rate(num_requests=3, period=3600)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            bot_token = env('BOT_TOKEN')
            chat_id = env('CHAT_ID')
            message = (f'Вопросы с главной страницы: {serializer.data["question_text"]}\n'
                       f'Контакты: {serializer.data["contact"]}\n'
                       f'Создано в: {str(serializer.data["created_at"])}')
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
            requests.post(url)

            headers = self.get_success_headers(serializer.data)
            response_201 = {
                "message": _("Ваш запрос успешно отправлен! Менеджер свяжется с вами в ближайшее время."),
            }
            return Response(response_201, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            response_400 = {
                "message": _("Ваш запрос не был успешно отправлен! Пожалуйста, попробуйте позже. Ошибка: {}").format(
                    str(e))
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)


class OurTeamCreateView(generics.CreateAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


class OurTeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = QuestionList.objects.all()
    serializer_class = QuestionListSerializer


class QuestionListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionList.objects.all()
    serializer_class = QuestionListSerializer
