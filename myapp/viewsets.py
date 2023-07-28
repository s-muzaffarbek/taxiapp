from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from myapp.models import Driver, Passenger, Road, Car, Station
from myapp.serializers import DriverSerializer, PassengerSerializer, RoadSerializer, CarSerializer, StationSerializer


class DriverAPIView(ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

class PassengerAPIView(ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()

class RoadAPIView(ModelViewSet):
    serializer_class = RoadSerializer
    queryset = Road.objects.all()

class CarAPIView(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class StationAPIView(ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

