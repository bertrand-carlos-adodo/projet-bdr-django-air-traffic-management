from django.db import models

class Country(models.Model):
    country_id = models.IntegerField(unique=True, primary_key=True)
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.country_name)

class City(models.Model):
    city_id = models.IntegerField(unique=True,primary_key=True)
    city_name = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.city_name)

class Airport(models.Model):
    airport_id = models.IntegerField(unique=True, primary_key=True)
    airport_name = models.CharField(max_length=150)
    longitude = models.FloatField()
    latitude = models.FloatField()
    altitude = models.FloatField()
    timezone1 = models.FloatField()
    timezone2 = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.airport_name, self.timezone2)

class Plane(models.Model):
    plane_id = models.IntegerField(unique=True, primary_key=True)
    plane_name = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.plane_name)

class Airline(models.Model):
    airline_id = models.IntegerField(unique=True, primary_key=True)
    airline_name = models.CharField(max_length=150)
    airline_actif = models.BooleanField()
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.airline_name)

class Routes(models.Model):
    routes_id = models.IntegerField(unique=True,primary_key=True)
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    airport_id_source = models.ForeignKey(Airport, related_name='airport_id_source', on_delete=models.CASCADE)
    airport_id_dest = models.ForeignKey(Airport, on_delete=models.CASCADE)
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s' % (self.airport_id_source, self.airport_id_dest)
