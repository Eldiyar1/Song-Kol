from django.urls import path
from .views import (
    CommentViewListCreate,
    CommentViewRetrieveUpdateDestroy,
    PhotoListCreateView,
    PhotoRetrieveUpdateDestroyView
)

urlpatterns = [
    path('comment/', CommentViewListCreate.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/', CommentViewRetrieveUpdateDestroy.as_view(), name='comment-detail'),
    path('photo/', PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photo/<int:pk>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo-detail'),
]
