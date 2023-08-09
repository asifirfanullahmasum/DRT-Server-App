from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .helpers.mapHelper import *
from .helpers.busAllocationHelper import *
from .helpers.googleAPIHelper import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

# Create your views here. 
def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def services(request):
    map = intializeMap()
    
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        location = extractGeocodes(vehicle.veh_location)
        map = addBusMarker(map, location,  color='blue')

    if request.method == 'POST':
        origin = request.POST.get('pickup')
        destination = request.POST.get('dropoff')

        bus_location, origin, origin_address, destination, destination_address, path, duration, waypoints = preprocess(origin, destination, vehicles)
        map = displayRoute(map, bus_location, origin, origin_address, destination, destination_address, path, duration, waypoints)
    
    context = {'map': map._repr_html_()}
    return render(request, 'services.html', context)

@api_view(['GET'])
def getTrips(request):
    trips = Trip.objects.all()
    serializer = TripSerializer(trips, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def rideRequest(request):
    data = request.data
    pickup = data['pickup']
    dropoff = data['dropoff']
    trip = createTrip(pickup, dropoff)
    serializer = TripSerializer(trip, many=False)
    
    return Response(serializer.data)
