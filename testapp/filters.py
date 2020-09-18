from listings.models import listing_model
import django_filters

class UserFilter(django_filters.FilterSet):
    #price = django_filters.NumberFilter()
   # Max_price = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    Min_price = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = listing_model
        fields = ('title', 'city', 'Min_price')