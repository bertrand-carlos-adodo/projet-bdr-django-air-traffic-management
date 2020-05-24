from django.urls import path
from . import views

app_name = 'trafic'

urlpatterns = [
    path('statistique/', views.statistique, name = 'statistique'),
    path('plan/', views.plan, name = 'plan'),
    path('trafic/', views.densite, name = 'densite'),
    path('airline/', views.show_airline, name = 'entite'),
    path('airport/', views.show_airport, name = 'airport'),
    path('city/', views.show_city, name = 'city'),
    path('country/', views.show_pays, name = 'pays'),
    path('plane/', views.show_avion, name = 'avion'),
    path('itineraires/', views.show_routes, name = 'routes'),
    path('compagni_desserant/', views.compagniedesservant, name = 'compagniedesservant')
]
