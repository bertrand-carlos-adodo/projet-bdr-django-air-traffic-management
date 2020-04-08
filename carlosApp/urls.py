from django.urls import path
from . import views

app_name = 'trafic'

urlpatterns = [
    path('plan/', views.plan, name = 'plan'),
    path('densite/', views.densite, name = 'densite'),
    path('entite/', views.entite, name = 'entite'),
]
