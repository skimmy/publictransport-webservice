'''
Created on Apr 17, 2013

@author: Michele Schimd
'''

# Haversine formula example in Python
# Author: Wayne Dyck

import math
import constants

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = constants.EARTH_MEAN_RADIUS_METERS # meters

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def findMeanPoint(points):
    """Computes the geographic point P such that it is the mean
    between all the points passed as parameter"""
    n = float(len(points))
    lat = 0.0
    lon = 0.0
    for p in points:
        lat += p[0]
        lon += p[1]
    return (lat / n, lon / n)

def findMinMaxDistance(pRef, pList):
    if len(pList) < 1:
        return None 
    dmax = dmin = distance((pRef[0], pRef[1]),
                       (pList[0][0], pList[0][1]))
    for p in pList:
        d = distance((pRef[0], pRef[1]),
                           (p[0], p[1]))
        if d < min:
            dmin = d
        if d > max:
            dmax = d
        return (dmin,dmax)

if __name__ == "__main__":
    seattle = [47.621800, -122.350326]
    olympia = [47.041917, -122.893766]
    print distance(seattle, olympia)
    print findMeanPoint([seattle, olympia])