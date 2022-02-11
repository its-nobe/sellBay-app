import django_filters
from .models import *
from django_filters import CharFilter, NumberFilter

class ListingFilter (django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    category = CharFilter(field_name='category', lookup_expr='icontains', label='Category')
    min_price = NumberFilter(field_name='price', lookup_expr='gte', label='Minimum Price')
    max_price = NumberFilter(field_name='price', lookup_expr='lte', label='Maximum Price')
    
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['owner', 'description', 'time', 'link', 'price']