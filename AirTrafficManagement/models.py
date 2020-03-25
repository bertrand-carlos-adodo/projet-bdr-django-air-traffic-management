from django.db import models

# Create your models here.

class Contry(models.Model):
    name_contry=models.CharField(max_length=50)

class City(models.Model):
    name_city=models.CharField(max_length=50)
    clé_contry=models.ForeignKey(Contry,on_delete=models.CASCADE)
    
class Airoport(models.Model):
    name_airoport=models.CharField(max_length=200)
    ville=models.CharField(max_length=200)
    latitude=models.IntegerField()
    latitude=models.IntegerField()
    timezone1=models.IntegerField()
    timezone2=models.IntegerField()
    clé_city=models.ForeignKey(City,on_delete=models.CASCADE)
    
class Airline(models.Model):
    name_airline=models.CharField(max_length=200)
    clé_contry=models.ForeignKey(Contry,on_delete=models.CASCADE)

class Plane(models.Model):
    name_plane=models.CharField(max_length=200)
    code_IATA=models.CharField(max_length=20)
    code_OACI=models.CharField(max_length=20)
    clé_airline=models.ForeignKey(Contry,on_delete=models.CASCADE)
class Ligne(models.Model):
    clé_airline=models.ForeignKey(Airline,on_delete=models.CASCADE)
    clé_airoport_dep=models.ForeignKey(Airoport,on_delete=models.CASCADE)
    clé_airoport_=models.ForeignKey(Airoport,related_name="airoportarr",on_delete=models.CASCADE)
    ligne_direct=models.BooleanField(default=True)