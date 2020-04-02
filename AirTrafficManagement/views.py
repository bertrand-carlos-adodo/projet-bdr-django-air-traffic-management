from django.shortcuts import render

def home(request):
	return render(request, 'pages/home.html')

def statistique(request):
	return render(request, 'pages/statistique.html')

def authentification(request):
	return render(request, 'pages/authentification.html')

def handler404(request, exception):
	return render(request, 'errors/404.html', {'error' : exception}, status = 404)

def handler500(request, exception = None):
	return render(request, 'errors/500.html', {}, status = 500)
