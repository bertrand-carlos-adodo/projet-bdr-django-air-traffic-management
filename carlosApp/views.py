from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import Http404


@login_required
def show_airline(request):
    name=request.POST.get('your_name',False)
    etat = request.POST.getlist('etat')
    if not name:
        
        if etat==[]:
            airlines = Airline.objects.all()
        else:
            if "actif" in etat:
                airlines=Airline.objects.filter(airline_actif=True)
            if  "inactif" in etat:
                airlines=Airline.objects.filter(airline_actif=False)
        
    else:
        try:
           country=Country.objects.get(country_name=name)
        except Country.DoesNotExist:
            raise Http404("Sorrye,Country #{} n'est pas un pays".format(name))
        
        
        if etat==[]:
            airlines=Airline.objects.filter(country_id=country.country_id)
        else:
            if "actif" and "inactif" in etat:
                airlines=Airline.objects.filter(country_id=country.country_id)
            if "actif" in etat:
                airlines=Airline.objects.filter(country_id=country.country_id,airline_actif=True)
            if  "inactif" in etat:
                airlines=Airline.objects.filter(country_id=country.country_id,airline_actif=False)
   
    
    return render(request, 'trafic/entite.html', {'airlines': airlines})


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
