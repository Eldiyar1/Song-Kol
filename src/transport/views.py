from rest_framework import permissions, generics

from .models import CarRental, Taxi
from .serializers import CarRentalSerializer, TaxiSerializer


class CarRentalListCreateView(generics.ListCreateAPIView):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarRentalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaxiListCreateView(generics.ListCreateAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaxiRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
