from django.urls import path, include
from rest_framework import routers

from .views import (
    TourAddViewSet,
    TourProgramViewSet,
    PriceViewSet,
    TipsViewSet,
    PhotoViewSet,
    TourDateViewSet,
    BookingGroupTourViewSet,
    BookingPrivateTourViewSet, PriceDetailsCreateViewSet, PriceDetailsViewSet,
)

router = routers.DefaultRouter()
router.register(r'TourAdd', TourAddViewSet)
router.register(r'TourProgram', TourProgramViewSet)
router.register(r'Price', PriceViewSet)
router.register(r'Tips', TipsViewSet)
router.register(r'PhotoComment', PhotoViewSet)
router.register(r'TourDate', TourDateViewSet)
router.register(r'BookingGroupTour', BookingGroupTourViewSet)
router.register(r'BookingPrivateTour', BookingPrivateTourViewSet)
router.register(r'PriceDetailsCreate', PriceDetailsCreateViewSet, basename='price_details_create')
router.register(r'PriceDetails', PriceDetailsViewSet)
# router.register(r'TourDateCreate', TourDatesCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('PriceDetails/', views.PriceAPIView.as_view())
]