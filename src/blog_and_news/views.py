from rest_framework import viewsets, status, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .serializers import BlogSerializer, SlidesImagesSerilaizer

from .models import BlogNews

from .filters import BlogFilter


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogNews.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BlogFilter
    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'category']


class SliderViewSet(viewsets.ModelViewSet):
    queryset = BlogNews.objects.all()
    serializer_class = SlidesImagesSerilaizer

    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]
