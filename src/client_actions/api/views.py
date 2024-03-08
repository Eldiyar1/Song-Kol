from rest_framework import generics, permissions

from rest_framework.pagination import LimitOffsetPagination

from client_actions.models import Comment, PhotoComment
from client_actions.api.serializers import CommentSerializer, PhotoSerializer

from client_actions.services.comment_moderation import CommentService


class CommentViewListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all().prefetch_related('photos')
    serializer_class = CommentSerializer
    filterset_fields = ['is_approved']
    ordering_fields = ['-created_at', 'stars']
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return CommentService.create_comment(self, request)


class CommentViewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().prefetch_related('photos')
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return CommentService.update_comment(self, request)


class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = PhotoComment.objects.all()
    serializer_class = PhotoSerializer


class PhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhotoComment.objects.all()
    serializer_class = PhotoSerializer
