from rest_framework import serializers

from .compress_image import compress_image
from .models import CommentView, PhotoComment


class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.FileField()

    class Meta:
        ref_name = "CommentsPhoto"
        model = PhotoComment
        fields = '__all__'

    def create(self, validated_data):
        return PhotoComment.objects.create(**validated_data)


class CommentViewSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False, read_only=True)
    upload_images = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only = True
    )

    class Meta:
        model = CommentView
        fields = ['id', 'stars', 'name', 'text', 'photos', 'tour', 'date', 'is_approved', 'upload_images']
        read_only_fields = ('id', 'date', 'is_approved', 'photos')
        extra_kwargs = {
            "tour": {"required": False},
            "id": {"required": False}
        }

    def create(self, validated_data):
        photos_data = validated_data.pop('upload_images', [])
        comment = CommentView.objects.create(**validated_data)
        for photo_data in photos_data:
            photo_data = compress_image(photo_data)
            PhotoComment.objects.create(comment=comment, photo=photo_data)
        return comment

    def to_representation(self, instance):
        data = super().to_representation(instance)
        tour_name = instance.tour.name if instance.tour else None
        data['tour'] = tour_name
        data['photos'] = [{photo.photo.url} for photo in instance.photos.all()]

        return data