import os
import requests
try:
    from gunicorn.config import User
except ModuleNotFoundError:
    User = None

from rest_framework import viewsets, status, permissions
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


class CommentViewViewSet(viewsets.ModelViewSet):
    queryset = CommentView.objects.all()
    serializer_class = CommentViewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter
    ordering_fields = ['-date', 'stars']
    allowed_actions = ['create', 'list', 'retrieve']


    # Add pagination class
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            queryset = self.filter_queryset(self.get_queryset().filter(is_approved=True))

            # Apply pagination
            paginated_queryset = self.paginate_queryset(queryset)

            serializer = self.get_serializer(paginated_queryset, many=True)

            # Return paginated response
            return self.get_paginated_response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)

    def get_queryset(self):
        qs = CommentView.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(is_approved=True)
        return qs

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data["is_approved"] = False
        mutable_data["at_moderation"] = timezone.now()
        serializer = CommentViewSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Спасибо за ваш отзыв! Ваш комментарий был успешно отправлен на модерацию и будет опубликован, как только пройдет проверку."
            }
            headers = self.get_success_headers(serializer.data)
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        response_data = {
            "message": "Упс! Что-то пошло не так. Разработчики уже работают над исправлением, и вы сможете добавить комментарии снова.",
            "data": serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        mutable_data = request.data.copy()
        mutable_data["is_approved"] = request.data.get("is_approved", instance.is_approved)

        if not instance.is_approved and instance.moderated_at is not None:
            two_days_ago = timezone.now() - timedelta(days=2)
            if instance.moderated_at <= two_days_ago:
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CommentViewSerializer(instance, data=mutable_data)
        if serializer.is_valid() and isinstance(request.user and request.user.is_staff, User):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_staff:  # Check if the user is an admin
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        response_403 = {
            "message": "Insufficient permissions! Only admins can delete comments."
        }
        return Response(response_403, status=status.HTTP_403_FORBIDDEN)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = PhotoComment.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
