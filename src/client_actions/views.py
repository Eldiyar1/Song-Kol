import os
import requests

try:
    from gunicorn.config import User
except ModuleNotFoundError:
    User = None

from rest_framework import viewsets, status, permissions, generics
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import timedelta
from django.utils import timezone
from rest_framework.pagination import LimitOffsetPagination
from django.utils.translation import gettext_lazy as _

from .compress_image import compress_image
from .filters import CommentFilter
from .models import (
    CommentView,
    PhotoComment
)

from .serializers import (
    CommentViewSerializer,
    PhotoSerializer

)


class CommentViewListCreate(generics.ListCreateAPIView):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['is_approved']
    ordering_fields = ['-date', 'stars']
    pagination_class = LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            queryset = self.filter_queryset(self.get_queryset().filter(is_approved=True))
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = self.get_serializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data["is_approved"] = False
        mutable_data["at_moderation"] = timezone.now()
        serializer = CommentViewSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": _("Спасибо за ваш отзыв! Ваш комментарий был успешно отправлен на модерацию и будет "
                             "опубликован, как только пройдет проверку.")
            }
            headers = self.get_success_headers(serializer.data)
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        response_data = {
            "message": _(
                "Упс! Что-то пошло не так. Разработчики уже работают над исправлением,"
                "и вы сможете добавить комментарии снова."),
            "data": serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class CommentViewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        mutable_data = request.data.copy()
        mutable_data["is_approved"] = request.data.get("is_approved", instance.is_approved)

        if not instance.is_approved and instance.at_moderation is not None:
            two_days_ago = timezone.now() - timedelta(days=2)
            if instance.at_moderation <= two_days_ago:
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CommentViewSerializer(instance, data=mutable_data)
        if serializer.is_valid() and request.user.is_staff:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        response_403 = {
            "message": _("Недостаточно прав! Удалять комментарии могут только администраторы.")
        }
        return Response(response_403, status=status.HTTP_403_FORBIDDEN)


class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = PhotoComment.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhotoComment.objects.all()
    serializer_class = PhotoSerializer
