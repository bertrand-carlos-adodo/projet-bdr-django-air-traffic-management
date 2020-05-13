from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def connexion(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and User.is_active is True:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            context['error'] = "Nom d'utilisateur ou mot de passe incorrect ou utilisateur non actif !!"
            return render(request, 'pages/login.html', context)
    else:
        return render(request, 'pages/login.html', context)

@login_required
def home(request):
    context = {}
    context['user'] = request.user
    return render(request, 'pages/home.html', context)

def deconnexion(request):
    logout(request)
    return HttpResponseRedirect(reverse('connexion'))

@login_required
def authentification(request):
    return render(request, 'pages/authentification.html')

def handler404(request, exception):
    return render(request, 'errors/404.html', {'error': exception}, status=404)

def handler500(request, exception=None):
    return render(request, 'errors/500.html', {}, status=500)
