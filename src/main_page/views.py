import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
import time
from functools import wraps
from rest_framework.viewsets import ModelViewSet

from .models import FormQuestion, OurTeam, QuestionList
from .serializers import FormQuestionSerializer, OurTeamSerializer, QuestionListSerializer


def limit_rate(num_requests, period):
    def decorator(view_func):
        request_history = []

        @wraps(view_func)
        def wrapped_view(*args, **kwargs):
            current_time = time.time()

            # Очистка истории запросов, удаляющая старые записи
            request_history[:] = [timestamp for timestamp in request_history if timestamp > current_time - period]

            if len(request_history) >= num_requests:
                # Достигнуто ограничение частоты запросов
                responce_len_ratelimit = {
                    "message": "Rate limit exceeded",
                }
                return Response(responce_len_ratelimit, status=status.HTTP_429_TOO_MANY_REQUESTS)

            request_history.append(current_time)
            return view_func(*args, **kwargs)

        return wrapped_view

    return decorator


class FormQuestionViewSet(viewsets.ModelViewSet):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

    @limit_rate(num_requests=3, period=3600)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # Отправка данных в телеграмм
            bot_token = '5964377497:AAEXxcJ745bQpNUpB2neHIjMMkf0IBF5mn4'
            chat_id = '860389338'
            message = f'Вопросы с главной страницы: {serializer.data["question_text"]}\nКонтакты: {serializer.data["contact"]}\n Создано в: {str(serializer.data["created_at"])}'
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
            requests.post(url)

            headers = self.get_success_headers(serializer.data)
            responce_201 = {
                "message": "Your request has been successfully submitted!  Manager will contact you soon.",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED, headers=headers)
        except Exception:
            responce_400 = {
                "message": "Your request has not been successfully submitted!  Please try again later."
            }

            return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)


class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            responce_201 = {
                "message": "Employee has been successfully created!",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionListViewSet(viewsets.ModelViewSet):
    queryset = QuestionList.objects.all()
    serializer_class = QuestionListSerializer

