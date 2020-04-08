from django.shortcuts import render

def plan(request):
    	return render(request, 'trafic/plan.html')

def densite(request):
    	return render(request, 'trafic/densite.html')

def entite(request):
    	return render(request, 'trafic/entite.html')
