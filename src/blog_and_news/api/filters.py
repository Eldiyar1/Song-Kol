from django_filters import rest_framework as filters

from blog_and_news.models import BlogNews


class BlogNewsFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = BlogNews
        fields = ['title', 'category']
