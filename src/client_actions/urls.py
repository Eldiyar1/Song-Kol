from django.urls import path, include
from rest_framework import routers
from .views import CommentViewViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewViewSet)
router.register(r'photo', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
