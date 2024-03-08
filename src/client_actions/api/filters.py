import django_filters
from client_actions.models import CommentView


class CommentFilter(django_filters.FilterSet):
    tour = django_filters.NumberFilter(field_name='tour')

    class Meta:
        model = CommentView
        fields = ('tour',)
