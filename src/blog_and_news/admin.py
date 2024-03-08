from django.contrib import admin
from django_summernote import admin as sadmin
from .models import BlogNews, Slides


class SlidesAdmin(admin.TabularInline):
    model = Slides
    fields = ["slides"]
    extra = 5


@admin.register(BlogNews)
class BlogNewsAdmin(sadmin.SummernoteModelAdmin):
    list_display = ('title', 'category', 'created_at')
    summernote_fields = ('content',)
    inlines = [SlidesAdmin, ]
    ordering = ('-created_at',)

