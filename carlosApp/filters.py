import django_filters
from django_filters import CharFilter

from .models import *


class PlaneFilter(django_filters.FilterSet):
    plane = CharFilter(field_name='plane_name',
                       lookup_expr='icontains', label="Nom de l'avion")

    class Meta:
        model = Plane
        fields = []


class PaysFilter(django_filters.FilterSet):
    pays = CharFilter(field_name='country_name',
                      lookup_expr='icontains', label="Nom du pays")

    class Meta:
        model = Country
        fields = []


class AirlineFilter(django_filters.FilterSet):
    compagnie = CharFilter(field_name='airline_name',
                           lookup_expr='icontains', label='Nom')

    class Meta:
        model = Airline
        fields = ['country_id', 'airline_actif']

    def __init__(self, *args, **kwargs):
        super(AirlineFilter, self).__init__(*args, **kwargs)
        self.filters['country_id'].label = "Pays"
        self.filters['airline_actif'].label = "Actif"


class CityFilter(django_filters.FilterSet):
    ville = CharFilter(field_name='city_name',
                       lookup_expr='icontains', label='Nom de la ville')

    class Meta:
        model = City
        fields = ['country_id']

    def __init__(self, *args, **kwargs):
        super(CityFilter, self).__init__(*args, **kwargs)
        self.filters['country_id'].label = "Pays"


class AirportFilter(django_filters.FilterSet):
    airport = CharFilter(field_name='airport_name',
                         lookup_expr='icontains', label='Nom')

    class Meta:
        model = Airport
        fields = ['city_id']

    def __init__(self, *args, **kwargs):
        super(AirportFilter, self).__init__(*args, **kwargs)
        self.filters['city_id'].label = "Ville"

class RoutesFilter(django_filters.FilterSet):

    class Meta:
        model = Routes
        fields = ['airline_id']

    def __init__(self, *args, **kwargs):
        super(RoutesFilter, self).__init__(*args, **kwargs)
        self.filters['airline_id'].label = "Compagnie"

