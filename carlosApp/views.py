from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Airline

def show_airline(request):
    	airline = Airline.objects.all()
    	return render(request, {'airline':airline})

@login_required
def plan(request):
    	return render(request, 'trafic/plan.html')

@login_required
def densite(request):
    	return render(request, 'trafic/densite.html')

@login_required
def entite(request):
    	return render(request, 'trafic/entite.html')
