from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import BlogSerializer, SlidesImagesSerializer
from .models import BlogNews
from .filters import BlogFilter


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BlogFilter
    search_fields = ['title', 'category']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SliderListCreateView(generics.ListCreateAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = SlidesImagesSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SliderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogNews.objects.all()
    serializer_class = SlidesImagesSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
