from django.urls import path
from . import views

app_name = 'trafic'

urlpatterns = [
    path('plan/', views.plan, name = 'plan'),
    path('densite/', views.densite, name = 'densite'),
    path('entite/', views.entite, name = 'entite'),
    path('entite/airline/', views.get_airline, name = 'entite/airline'),
    path('entite/villes/', views.get_ville, name = 'entite/villes'),
    path('entite/pays/', views.get_pays, name = 'entite/pays'),
    path('entite/aeroports/', views.get_aeroport, name = 'entite/aeroports'),
    path('entite/avions/', views.get_plane, name = 'entite/avions'),
]
