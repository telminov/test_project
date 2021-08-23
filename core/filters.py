import django_filters

from core import models


class Book(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='istartswith')

    class Meta:
        model = models.Book
        fields = ('name', )

