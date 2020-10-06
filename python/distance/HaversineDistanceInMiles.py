import math

def distanceInMilesOrKilos(milesOrKilos,originLat,originLon,destinationLat,destinationLon):    
    radius = 3959 if milesOrKilos == "miles" else 6371
    
    lat1 = originLat
    lat2 = destinationLat
    lon1 = originLon
    lon2 = destinationLon     

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance