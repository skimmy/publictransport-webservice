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

if __name__ == "__main__":
    seattle = [47.621800, -122.350326]
    olympia = [47.041917, -122.893766]
    casa = [45.549313,12.07541]
    nuovacasa = [45.551777,12.076697]
    print distance(seattle, olympia)
    print distance(casa, nuovacasa)