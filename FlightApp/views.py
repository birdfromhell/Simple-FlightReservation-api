from django.shortcuts import render
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializers, PassengerSerializers, ReservationSerializers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    Reservation.save(reservation)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def findFlight(request):
    flight = Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'],
                                   dateOfDeparture=request.data['dateOfDeparture'])
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


def index(request):
    return HttpResponseRedirect('api/')
