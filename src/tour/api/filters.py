from django_filters import rest_framework as filters

from tour.models import TourAdd


class TourAddFilter(filters.FilterSet):
    keyword = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = TourAdd
        fields = ('keyword',)
        ordering = ('name',)
