from django.urls import path, include
from rest_framework import routers
from .views import (
    CarRentalViewSet,
TaxiViewSet
)

router = routers.DefaultRouter()
router.register(r'CarRental', CarRentalViewSet)
router.register(r'Taxi', TaxiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
