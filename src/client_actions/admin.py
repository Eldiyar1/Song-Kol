from django.contrib import admin
from django.utils.html import format_html

from .models import (
    CommentView,
    PhotoComment
)

admin.site.register(PhotoComment)


class PhotoInline(admin.TabularInline):
    model = PhotoComment
    extra = 0


@admin.register(CommentView)
class CommentViewAdmin(admin.ModelAdmin):
    list_display = ('stars', 'name', 'text', 'date')
    list_filter = ('date', 'stars')
    inlines = [PhotoInline]
