from django.urls import path
from .views import BlogListCreateView, BlogRetrieveUpdateDestroyView, SliderListCreateView, \
    SliderRetrieveUpdateDestroyView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view(), name='blog-retrieve-update-destroy'),
    path('sliders/', SliderListCreateView.as_view(), name='slider-list-create'),
    path('sliders/<int:pk>/', SliderRetrieveUpdateDestroyView.as_view(), name='slider-retrieve-update-destroy'),
]
