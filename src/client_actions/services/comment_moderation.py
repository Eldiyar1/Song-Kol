from copy import copy
from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from client_actions.api.serializers import CommentSerializer


class CommentService:
    @staticmethod
    def create_comment(self, request):
        mutable_data = copy(request.data)
        mutable_data["is_approved"] = False
        mutable_data["at_moderation"] = timezone.now()
        serializer = CommentSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": _("Спасибо за ваш отзыв! Ваш комментарий был успешно отправлен на "
                             "модерацию и будет опубликован, как только пройдет проверку.")
            }
            headers = self.get_success_headers(serializer.data)
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        response_data = {
            "message": _("Упс! Что-то пошло не так. Разработчики уже работают над исправлением, "
                         "и вы сможете добавить комментарии снова."),
            "data": serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update_comment(self, request):
        instance = self.get_object()
        mutable_data = copy(request.data)
        mutable_data["is_approved"] = request.data.get("is_approved", instance.is_approved)

        if not instance.is_approved and instance.at_moderation is not None:
            two_days_ago = timezone.now() - timedelta(days=2)
            if instance.at_moderation <= two_days_ago:
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CommentSerializer(instance, data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
