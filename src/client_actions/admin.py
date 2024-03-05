from django.contrib import admin
from django.utils.html import format_html

from .models import Comment, PhotoComment


class PhotoInline(admin.TabularInline):
    model = PhotoComment
    extra = 5


@admin.register(Comment)
class CommentViewAdmin(admin.ModelAdmin):
    list_display = ('stars', 'name', 'text', 'created_at')
    list_filter = ('created_at', 'stars')
    inlines = [PhotoInline]
    ordering = ('-created_at',)

