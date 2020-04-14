from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import Http404

def get_airline(request):
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
                
            
    return render(request,"trafic/compagnie.html", {'compagnies':airlines})




def get_ville(request):
    citys=City.objects.all()
    return render(request,"trafic/ville.html", {'villes':citys})
def get_aeroport(request):
    aeroports=Airport.objects.all()[:30]
    return render(request,"trafic/aeroport.html", {'aeroports':aeroports})
   
def get_plane(request):
    name=request.POST.get('your_name',False)
    if not name:
        planes=Plane.objects.all()
    else:
        planes=Plane.objects.filter(plane_name__contains=name)  
    
    return render(request,"trafic/plane.html", {'planes':planes,'your_name':name})

def get_pays(request):
    pays=Country.objects.all()
    return render(request,"trafic/pays.html", {'pays':pays})
    
@login_required
def plan(request):
    	return render(request, 'trafic/plan.html')

@login_required
def densite(request):
    	return render(request, 'trafic/densite.html')

@login_required
def entite(request):
    	return render(request, 'trafic/entite.html')
