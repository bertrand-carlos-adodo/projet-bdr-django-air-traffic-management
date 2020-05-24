from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *


@login_required
def statistique(request):
    sairline = Airline.objects.all()
    sairport = Airport.objects.all()
    scity = City.objects.all()
    spays = Country.objects.all()
    savion = Plane.objects.all()
    sroutes = Routes.objects.all()
    context = {'sairline': sairline, 'sairport': sairport, 'scity': scity,
               'spays': spays, 'savion': savion, 'sroutes': sroutes}
    return render(request, 'trafic/statistique.html', context)


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
    route = Routes.objects.all()
    routesfilter = RoutesFilter(request.GET, queryset=route)
    route = routesfilter.qs
    return render(request, 'trafic/plan.html', {'route': route[:100], 'routes': route,
                                                'routesfilter': routesfilter})


@login_required
def compagniedesservant(request):
    pays = Country.objects.all()
    paysfilter = PaysFilter(request.GET, queryset=pays)
    pays = paysfilter.qs
    id_pays = list(pays.values_list('country_id', flat=True))[0]
    citys = City.objects.filter(country_id=id_pays)
    airports = []
    for city in citys:
        airports.append(Airport.objects.filter(city_id=city))
    lignes = []
    filtre_lignes = []
    for airport in airports:
        airport_id = list(airport.values_list('airport_id', flat=True))[0]
        lignes.append(Routes.objects.filter(airport_id_dest=airport_id))
    for ligne in lignes:
        if list(ligne) != []:
            filtre_lignes.append(ligne)
    results = []
    for filtre in filtre_lignes:
        for fil in filtre:
            results.append(fil)
    return render(request, 'trafic/com_desservant.html', {'paysfilter': paysfilter, 'results': results})


@login_required
def densite(request):
    return render(request, 'trafic/densite.html')


@login_required
def entite(request):
    return render(request, 'trafic/entite.html')
