from math import sqrt
from .mapHelper import *
from .googleAPIHelper import *
from ..models import *
from datetime import date, datetime, timedelta


def preprocess(origin, destination, vehicles):
    addr_ext = ', Kalamazoo, Michigan, USA'
    origin = origin + addr_ext
    destination = destination + addr_ext
    waypoints = []

    origin = generateAddressDetails(origin)
    destination = generateAddressDetails(destination)

    trip = addTrip(origin, destination, vehicles)
    allocatedBus = trip.vehicle
    bus_location = extractGeocodes(allocatedBus.veh_location)
    trip_set = Trip.objects.filter(vehicle=allocatedBus)
    if trip_set:
        for otherTrip in trip_set:
            if otherTrip != trip:
                trip_dropoff = [
                    float(coord) for coord in otherTrip.dropoffgeocode.strip('()').split(',')]
                waypoints.append(trip_dropoff)
    waypoints.append(list(origin['location']))
    path, duration = getDirections(
        bus_location, destination['location'], waypoints)

    return bus_location, origin['location'], origin['address'], destination['location'], destination['address'], path, duration, waypoints


def allocateBus(origin, destination, buses):
    bus_subset = findClosestBus(origin, buses)
    for bus in bus_subset:
        bus_info = buses.get(id=bus)
        trip_set = Trip.objects.filter(vehicle=bus_info)
        if trip_set:
            for trip in trip_set:
                trip_dropoff = [float(coord)
                                for coord in trip.dropoff.strip('()').split(',')]
                # trip_dropoff = trip.dropoff
                veh_loc = extractGeocodes(bus_info.veh_location)
                original_path, original_duration = getDirections(
                    veh_loc, trip_dropoff)
                detoured_path, detoured_duration = getDirections(
                    veh_loc, trip_dropoff, [origin])
                print("Original Duration: ", original_duration)
                print("Detoured Duration: ", detoured_duration)
                print('Breakpoint')
                if detoured_duration < 1.7 * original_duration:
                    return bus_info
        else:
            return bus_info
        
def tripIsValid(start, end, waypoints):
    original_path, original_duration = getDirections(start, end)
    detoured_path, detoured_duration = getDirections(start, end, waypoints)
    if detoured_duration < 1.7 * original_duration:
        return True
    else:
        return False


def addTrip(origin, destination, vehicles):
    # allocated_bus = allocateBus(origin, destination, vehicles)
    # driver = Driver.objects.first()
    # customer = Customer.objects.first()
    # current_time = datetime.now().time()

    trip = createTrip(origin, destination)
    return trip

    # trip = Trip(
    #     vehicle=allocated_bus,
    #     customer=customer,
    #     driver=driver,
    #     tripdate=date.today().isoformat(),
    #     triptype='Standard',
    #     pickup=origin,
    #     dropoff=destination,
    #     pickuptime=current_time.strftime('%H:%M:%S'),
    #     dropofftime=current_time.strftime('%H:%M:%S'),
    #     createdAt=date.today().isoformat(),
    #     status='Ongoing',
    #     fullcapacity=False
    # )
    # trip.save()
    # return trip


def findClosestBus(pickup, buses):
    distanceMatrix = getDistanceMatrix(pickup, buses)
    return distanceMatrix


def getDistanceMatrix(pickup, buses):
    distanceMatrix = {}
    for bus in buses:
        location = extractGeocodes(bus.veh_location)
        distance = calculateDistance(pickup, location)
        if distance < 5:
            distanceMatrix[bus.id] = distance
        distanceMatrix = {k: v for k, v in sorted(
            distanceMatrix.items(), key=lambda item: item[1])}
    print(distanceMatrix)
    return distanceMatrix


def calculateDistance(point1, point2):
    distance = sqrt((point2[0] - point1[0]) ** 2 +
                    (point2[1] - point1[1]) ** 2)
    return distance


def createTrip(pickup, dropoff):
    pickup = generateAddressDetails(pickup)
    dropoff = generateAddressDetails(dropoff)
    pickuplocation = list(pickup['location'])
    dropofflocation = list(dropoff['location'])
    veh_set = findNearestVehicles(location=pickuplocation)
    print(veh_set)
    for veh in veh_set:
        activetrips = Trip.objects.filter(vehicle=veh, status='Ongoing')
        vehiclelocation = extractGeocodes(veh.veh_location)
        waypoints = []

        if activetrips:
            for activetrip in activetrips:
                activepickup = extractGeocodes(activetrip.pickupgeocode)
                activedropoff = extractGeocodes(activetrip.dropoffgeocode)
                if activetrip.status == 'Arriving':
                    waypoints.extend([activepickup, pickuplocation])
                    if tripIsValid(vehiclelocation, activedropoff, waypoints):
                        print('Proceed')
                elif activetrip.status == 'Ongoing':
                    waypoints.append(pickuplocation)
                    if tripIsValid(vehiclelocation, activedropoff, waypoints):
                        print('Proceed')
            break

        else:
            arrivalpath, arrivalduration = getDirections(
                vehiclelocation, pickuplocation)
            droppath, dropduration = getDirections(
                pickuplocation, dropofflocation)

            trip = createNewTrip(pickup, dropoff, veh,
                                 arrivalduration, dropduration)
            return trip


def findNearestVehicles(location):
    veh_set = []
    vehicles = Vehicle.objects.filter(fullcapacity=False)
    distanceMatrix = getDistanceMatrix(location, vehicles)
    for vehicle in vehicles:
        if vehicle.id in distanceMatrix:
            veh_set.append(vehicle)
    return veh_set


def createNewTrip(pickup, dropoff, vehicle, pickupduration, travelduration):
    pickup_address = pickup['address']
    dropoff_address = dropoff['address']
    pickup_location = pickup['location']
    dropoff_location = dropoff['location']

    # For testing purpose
    customer = Customer.objects.first()
    driver = Driver.objects.first()

    current_time = datetime.now().time()
    pickupduration = timedelta(minutes=pickupduration)
    travelduration = timedelta(minutes=travelduration)
    arrivalduration = (datetime.combine(
        datetime.today(), current_time) + pickupduration).time()
    dropduration = (datetime.combine(datetime.today(),
                    arrivalduration) + travelduration).time()
    pickuptime = arrivalduration.strftime('%H:%M:%S')
    dropofftime = dropduration.strftime('%H:%M:%S')

    trip = Trip(
        vehicle=vehicle,
        customer=customer,
        driver=driver,
        tripdate=date.today().isoformat(),
        triptype='Standard',
        pickupaddress=pickup_address,
        dropoffaddress=dropoff_address,
        pickupgeocode=pickup_location,
        dropoffgeocode=dropoff_location,
        pickuptime=pickuptime,
        dropofftime=dropofftime,
        createdAt=date.today().isoformat(),
        status='Arriving',
    )
    trip.save()
    return trip


def updateTrip(trip, stops):
    print(trip)
    print(stops)
