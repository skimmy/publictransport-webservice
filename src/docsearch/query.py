'''
Created on 08/giu/2013

@author: Michele Schimd
'''

def getNeghborhoodStringQuery(lat, lon, radius, field):
    query = "distance(%s, geopoint(%s, %s)) < %s" % (field, str(lat), str(lon), str(radius))
    return query 
