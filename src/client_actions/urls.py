from django.urls import path
from client_actions.api.views import (
    CommentViewListCreate,
    CommentViewRetrieveUpdateDestroy,
    PhotoListCreateView,
    PhotoRetrieveUpdateDestroyView
)

urlpatterns = [
    path('comments/', CommentViewListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentViewRetrieveUpdateDestroy.as_view(), name='comment-detail'),
    path('photos/', PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photos/<int:pk>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo-detail'),
]
