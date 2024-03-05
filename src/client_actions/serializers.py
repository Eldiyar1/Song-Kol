from rest_framework import serializers

from .models import Comment, PhotoComment


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = ('id', 'photo')


class CommentSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False, read_only=True)
    upload_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'stars', 'name', 'text', 'tour', 'is_approved', 'photos', 'upload_images')
        read_only_fields = ('id', 'is_approved', 'photos')
        extra_kwargs = {
            "tour": {"required": False},
            "id": {"required": False}
        }

    def create(self, validated_data):
        photos_data = validated_data.pop('upload_images', [])
        comment = Comment.objects.create(**validated_data)
        for photo_data in photos_data:
            PhotoComment.objects.create(comment=comment, photo=photo_data)
        return comment
