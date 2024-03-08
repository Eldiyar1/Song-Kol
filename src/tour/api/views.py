from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from tour.api.serializers import (
    TourAddSerializer,
    TourProgramSerializer,
    PriceSerializer,
    TipsSerializer,
    BookingPrivateTourSerializer,
    BookingGroupTourSerializer,
    TourDatesSerializer, PriceDetailCreateSerializer, PriceDetailSerializer
)
from tour.models import (
    TourAdd,
    TourProgram,
    Price,
    Tips,
    TourDates,
    BookingGroupTour,
    BookingPrivateTour, PriceDetail,
)
from tour.api.filters import TourAddFilter
from tour.services.service import BookingGroupTourService, BookingPrivateTourService, TourProgramDUService, \
    PriceDetailsService


class TourAddListCreateAPIView(generics.ListAPIView):
    queryset = TourAdd.objects.all()
    serializer_class = TourAddSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TourAddFilter


class TourProgramListCreateView(generics.ListCreateAPIView):
    queryset = TourProgram.objects.all()
    serializer_class = TourProgramSerializer


class TourProgramDUView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourProgram.objects.all()
    serializer_class = TourProgramSerializer

    def list(self, request, *args, **kwargs):
        service_response, status_code = TourProgramDUService.get_tour_programs_list(request)
        return Response(service_response, status=status_code)


class PriceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceListCreateDUAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDetailsCreateAPIView(generics.CreateAPIView):
    serializer_class = PriceDetailCreateSerializer

    def create(self, request, *args, **kwargs):
        service_response, status_code = PriceDetailsService.create_price_detail(request.data)
        return Response(service_response, status=status_code)


class PriceDetailsAPIView(generics.ListAPIView):
    queryset = PriceDetail.objects.all()
    serializer_class = PriceDetailSerializer


class TipsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer


class TipsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer


class TourDateListCreateAPIView(generics.ListCreateAPIView):
    queryset = TourDates.objects.all()
    serializer_class = TourDatesSerializer


class BookingPrivateTourViewSet(generics.CreateAPIView):
    queryset = BookingPrivateTour.objects.all()
    serializer_class = BookingPrivateTourSerializer

    def create(self, request, *args, **kwargs):
        service_response, status_code = BookingPrivateTourService.create_booking(request.data)
        return Response(service_response, status=status_code)


class BookingGroupTourViewSet(generics.CreateAPIView):
    queryset = BookingGroupTour.objects.all()
    serializer_class = BookingGroupTourSerializer

    def create(self, request, *args, **kwargs):
        service_response, status_code = BookingGroupTourService.create_booking(request.data)
        return Response(service_response, status=status_code)
