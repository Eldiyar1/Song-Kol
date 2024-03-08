from rest_framework import generics, permissions

from transport.models import CarRental, Taxi
from transport.api.serializers import CarRentalSerializer, TaxiSerializer


class CarRentalListCreateView(generics.ListCreateAPIView):
    queryset = (CarRental.objects.all().select_related('car_with_driver', 'car_without_driver')
                .prefetch_related('photos'))
    serializer_class = CarRentalSerializer


class CarRentalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarRental.objects.all().prefetch_related('photos')
    serializer_class = CarRentalSerializer


class TaxiListCreateView(generics.ListCreateAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer


class TaxiRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
