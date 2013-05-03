'''
Created on Apr 4, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import model.position as posmodel

def getGAEGeoPositionedItem(item):
    return GAEGeoPositionedItem(position=ndb.GeoPt(lat = item.position.latitude,
                                                   lon = item.position.longitude),
                                accuracy = item.accuracy,
                                mid=item.id)


class GAEGeoPositionedItem(polymodel.PolyModel):
    
    mid = ndb.StringProperty()
    position = ndb.GeoPtProperty()
    # TODO: [DESIGN] Probably accuracy doesn't need to be indexed
    accuracy = ndb.FloatProperty(indexed=False)
    
    def toPositionedItem(self):
        p = posmodel.PositionedItem(posmodel.GeoPosition(lat = self.position.lat,
                                                         lon = self.position.lon),
                                                         self.mid)
        p.setAccuracy(self.accuracy)
        return p        
