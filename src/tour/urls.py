from django.urls import path, include
from rest_framework import routers

from tour.api import views

urlpatterns = [
    path('Tour/', views.TourAddListCreateAPIView.as_view()),
    path('TourProgram/', views.TourProgramListCreateView.as_view()),
    path('TourProgram/<int:pk>/', views.TourProgramDUView.as_view()),
    path('Price/', views.PriceListCreateAPIView.as_view()),
    path('Price/<int:pk>/', views.PriceListCreateDUAPIView.as_view()),
    path('PriceDetailCreate/', views.PriceDetailsCreateAPIView.as_view()),
    path('PriceDetail/', views.PriceDetailsAPIView.as_view()),
    path('Tips/', views.TipsListCreateAPIView.as_view()),
    path('Tips/<int:pk>/', views.TipsAPIView.as_view()),
    path('TourDate/', views.TourDateListCreateAPIView.as_view()),
    path('BookingPrivate/', views.BookingPrivateTourViewSet.as_view()),
    path('BookingGroupTour/', views.BookingGroupTourViewSet.as_view()),
]
