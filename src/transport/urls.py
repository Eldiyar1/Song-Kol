from django.urls import path
from transport.api.views import CarRentalListCreateView, CarRentalRetrieveUpdateDestroyView, TaxiListCreateView, \
    TaxiRetrieveUpdateDestroyView

urlpatterns = [
    path('car_rentals/', CarRentalListCreateView.as_view(), name='car_rental_list_create'),
    path('car_rentals/<int:pk>/', CarRentalRetrieveUpdateDestroyView.as_view(), name='car_rental_detail'),
    path('taxis/', TaxiListCreateView.as_view(), name='taxi_list_create'),
    path('taxis/<int:pk>/', TaxiRetrieveUpdateDestroyView.as_view(), name='taxi_detail'),
]
