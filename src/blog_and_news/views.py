from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import IsSuperuser
from .serializers import BlogSerializer, SlidesImagesSerializer
from .models import BlogNews
from .filters import BlogFilter


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BlogFilter
    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'category']


class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]


class SliderListCreateView(generics.ListCreateAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = SlidesImagesSerializer
    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]


class SliderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = SlidesImagesSerializer
    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]
