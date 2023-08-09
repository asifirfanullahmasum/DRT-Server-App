import googlemaps
gmaps = googlemaps.Client(key="AIzaSyBX4J8qNGeBi5KRnzcW9qE6ALhDDuqvPG4")  # Initialize the Google Maps client with your API key


def getDirections(origin, destination, waypoints=[]):

    directions_result = gmaps.directions(
        origin=origin,
        destination=destination,
        waypoints=waypoints,
    )

    if not directions_result:
        raise Exception(f"No route found between {origin} and {destination}")
    
    duration = 0
    route = directions_result[0]
    polyline = route["overview_polyline"]["points"]
    path = googlemaps.convert.decode_polyline(polyline)
    path = [(coord["lat"], coord["lng"]) for coord in path]
    for leg in route["legs"]:
        duration = duration + getDuration(leg["duration"]["text"])

    return path, duration

def getDuration(duration):
    parts = duration.split(" ")
    extracted = parts[0]
    return int(extracted)

def generateAddressDetails(address):
    address_details = {}
    try:
        location = gmaps.geocode(address)

        if location is not None:
            lat = location[0]["geometry"]["location"]["lat"]
            lng = location[0]["geometry"]["location"]["lng"]
            address_details["address"] = address
            address_details["location"] = (lat, lng)
    except Exception as e:
        # Handle the exception here
        print("Error occurred while geocoding the address: {}".format(e))

    return address_details