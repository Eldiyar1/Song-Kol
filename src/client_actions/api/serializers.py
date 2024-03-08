from rest_framework import serializers

from client_actions.models import Comment, PhotoComment


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = ('id', 'photo')


class CommentSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False, read_only=True)
    upload_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True, required=False
    )
    comment = serializers.CharField(source="photos.comment", write_only=True, required=False)
    created_at = serializers.DateTimeField(format='%d.%m.%y', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id', 'stars', 'name', 'text', 'tour', 'created_at', 'is_approved', 'photos', 'comment', 'upload_images'
        )
        read_only_fields = ('id', 'is_approved')
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
