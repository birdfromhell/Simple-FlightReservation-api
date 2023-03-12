from django.shortcuts import render
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializers, PassengerSerializers, ReservationSerializers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def findFlight(request):
    flight = Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
    serial = FlightSerializers(flight, many=True)

    return Response(serial.data)


# Create your views here.
class FlightViewSets(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers


class PassengerViewSets(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers


class ReservationViewSets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
