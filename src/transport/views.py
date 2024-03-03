import requests
from django.db.migrations import serializer
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
import telegram
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarRental, Taxi
from .serializers import CarRentalSerializer, TaxiSerializer


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class CarRentalViewSet(viewsets.ModelViewSet):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer
    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = CarRentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                'message': 'Car rental created successfully',
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        responce_400 = {

            'message': 'Car rental could not be created',
            'errors': serializer.errors,
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        car_rental = self.get_object()
        serializer = CarRentalSerializer(car_rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                'message': 'Car rental updated successfully',
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        responce_400 = {

            'message': 'Car rental could not be updated',
            'errors': serializer.errors,
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        car_rental = self.get_object()
        car_rental.delete()
        responce_204 = {
           'message': 'Car rental deleted successfully',
        }
        return Response(responce_204, status=status.HTTP_204_NO_CONTENT)


class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsSuperuser | permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = TaxiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                'message': 'Taxi created successfully',
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        responce_400 = {

            'message': 'Taxi could not be created',
            'errors': serializer.errors,
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        taxi = self.get_object()
        serializer = TaxiSerializer(taxi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce_201 = {
                'message': 'Taxi updated successfully',
            }
            return Response(responce_201, status=status.HTTP_201_CREATED)
        responce_400 = {

            'message': 'Taxi could not be updated',
            'errors': serializer.errors,
        }
        return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        taxi = self.get_object()
        taxi.delete()
        responce_204 = {
            'message': 'Taxi deleted successfully',
        }
        return Response(responce_204, status=status.HTTP_204_NO_CONTENT)
