import folium

def intializeMap():
    map = folium.Map(location=[42.2917, -85.5872], zoom_start=13)
    return map

def addMarker(map, location, address = "", duration = "", color = "red"):
    folium.Marker(location=location, icon=folium.Icon(icon="map-marker", prefix="fa", color=color),   popup=folium.Popup(
                f"<b>Location</b>: {address} | <b>Est. Duration</b>: {duration}",
                max_width=450,
            )).add_to(map)
    return map
    
    
def displayRoute(map, vehicle, origin, origin_address, destination, destination_address, path, duration = "", waypoints = []):
    
    if vehicle:
        addBusMarker(map, vehicle, color='green')
    if origin:
        addMarker(map, origin, origin_address, duration, color='green')
    if destination:
        addMarker(map, destination, destination_address, color='red')
    if len(waypoints):
        for waypoint in waypoints:
            addMarker(map, waypoint, color='green')
    folium.PolyLine(path, weight=2.5, opacity=1).add_to(map)
    map.fit_bounds([origin, destination])
    return map

def displayBuses(map, buses, ):
    if len(buses):
        for bus in buses:
            addBusMarker(map, bus, color="blue")

def addBusMarker(map, location, color):
    if len(location):
        folium.Marker(
            location=location,
            popup=folium.Popup(
                f"<b>Bus Location</b>: {location[0]}, {location[1]}",
                max_width=450,
            ),
            icon=folium.Icon(icon="bus", prefix="fa", color=color),
        ).add_to(map)
    return map

def extractGeocodes(geocode_string):
    geocodes = geocode_string.strip('()').split(',')
    latitude = float(geocodes[0].strip())
    longitude = float(geocodes[1].strip())
    return [latitude, longitude]