from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def show_airline(request):
    airline = Airline.objects.all()
    return render(request, 'trafic/entite.html', {'airline': airline[:200], 'airlines': airline})


@login_required
def show_airport(request):
    airport = Airport.objects.all()
    return render(request, 'trafic/airport.html', {'airport': airport[:200], 'airports': airport})


@login_required
def show_city(request):
    city = City.objects.all()
    return render(request, 'trafic/city.html', {'city': city[:100], 'cities': city})


@login_required
def show_pays(request):
    pays = Country.objects.all()
    return render(request, 'trafic/pays.html', {'pays': pays[:100], 'payss': pays})


@login_required
def show_avion(request):
    nom = request.POST.get('nom_avion', False)
    if not nom:
        avion = Plane.objects.all()
    else:
        avion = Plane.objects.filter(plane_name__contains=nom)
    return render(request, 'trafic/avion.html', {'avion': avion[:150], 'avions': avion, 'nom_avion': nom})


@login_required
def show_routes(request):
    routes = Routes.objects.all()
    return render(request, 'trafic/routes.html', {'route': routes[:200], 'routes': routes})


@login_required
def plan(request):
    return render(request, 'trafic/plan.html')


@login_required
def densite(request):
    return render(request, 'trafic/densite.html')


@login_required
def entite(request):
    return render(request, 'trafic/entite.html')
