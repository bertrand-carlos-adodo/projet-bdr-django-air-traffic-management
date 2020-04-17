from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
#from django.http import Http404
from .filters import AirlineFilter, AirportFilter, PlaneFilter, PaysFilter, CityFilter


@login_required
def show_airline(request):
    airline = Airline.objects.all()
    airlinefilter = AirlineFilter(request.GET, queryset=airline)
    airline = airlinefilter.qs
    return render(request, 'trafic/entite.html', {'airline': airline[:100],
                                                  'airlines': airline, 'airlinefilter': airlinefilter})


@login_required
def show_airport(request):
    airport = Airport.objects.all()
    airportfilter = AirportFilter(request.GET, queryset=airport)
    airport = airportfilter.qs
    return render(request, 'trafic/airport.html', {'airport': airport[:100],
                                                   'airports': airport, 'airportfilter': airportfilter})


@login_required
def show_city(request):
    city = City.objects.all()
    villefilter = CityFilter(request.GET, queryset=city)
    city = villefilter.qs
    return render(request, 'trafic/city.html', {'city': city[:100],
                                                'villefilter': villefilter, 'cities': city})


@login_required
def show_pays(request):
    pays = Country.objects.all()
    paysfilter = PaysFilter(request.GET, queryset=pays)
    pays = paysfilter.qs
    return render(request, 'trafic/pays.html', {'pays': pays[:100],
                                                'payss': pays, 'paysfilter': paysfilter})


@login_required
def show_avion(request):
    avion = Plane.objects.all()
    avionfilter = PlaneFilter(request.GET, queryset=avion)
    avion = avionfilter.qs
    return render(request, 'trafic/avion.html', {'avion': avion[:100],
                                                 'avionfilter': avionfilter, 'avions': avion})


@login_required
def show_routes(request):
    routes = Routes.objects.all()
    return render(request, 'trafic/routes.html', {'route': routes[:100], 'routes': routes})


@login_required
def plan(request):
    return render(request, 'trafic/plan.html')


@login_required
def densite(request):
    return render(request, 'trafic/densite.html')


@login_required
def entite(request):
    return render(request, 'trafic/entite.html')
