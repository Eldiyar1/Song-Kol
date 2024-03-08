from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers

from blog_and_news.models import BlogNews, Slides

from urllib.parse import unquote


class SlidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slides
        fields = ("id", "slides", 'blog_news')


class BlogNewsSerializer(serializers.ModelSerializer):
    slides = SlidersSerializer(many=True, required=False, read_only=True)
    upload_slides = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    created_at = serializers.DateTimeField(format='%d.%m.%y', read_only=True)
    content = serializers.SerializerMethodField()

    class Meta:
        model = BlogNews
        fields = ('id', 'title', 'category', 'created_at', 'image', 'content', 'slides', 'upload_slides')

    def get_content(self, obj):
        # Получение хоста из контекста запроса
        request = self.context.get('request')
        current_site = get_current_site(request)
        host = current_site.domain

        # Замена пути к изображению на полный URL-адрес с хостом и декодирование символов
        content = obj.content
        content_with_host = content.replace('/sr/media/', f'http://{host}/sr/media/')
        decoded_content = unquote(content_with_host)

        return decoded_content

    def create(self, validated_data):
        slides_data = validated_data.pop('upload_slides', [])
        blog_news = BlogNews.objects.create(**validated_data)
        for slide_data in slides_data:
            Slides.objects.create(blog_news=blog_news, slides=slide_data)
        return blog_news
