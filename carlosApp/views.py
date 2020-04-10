from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def plan(request):
    	return render(request, 'trafic/plan.html')

@login_required
def densite(request):
    	return render(request, 'trafic/densite.html')

@login_required
def entite(request):
    	return render(request, 'trafic/entite.html')
