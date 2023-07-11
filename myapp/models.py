from django.db import models

from user.models import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=13)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.first_name

    def fullname(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=13)

    def __str__(self):
        return self.user.first_name

class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    conditioner = models.BooleanField(default=False)
    car_number = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Road(models.Model):
    name = models.CharField(max_length=100)
    start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start_roads')
    end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end_roads')
    distance = models.DecimalField(max_digits=9, decimal_places=2)
    geopoint = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
