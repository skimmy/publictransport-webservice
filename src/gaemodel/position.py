'''
Created on Apr 4, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb

import model.position as posmodel
from gaemodel.base import GAEBaseModel

def getGAEGeoPositionedItem(item):
    return GAEGeoPositionedItem(position=ndb.GeoPt(lat = item.position.latitude,
                                                   lon = item.position.longitude),
                                mid=item.id)


class GAEGeoPositionedItem(GAEBaseModel):
    position = ndb.GeoPtProperty()
    
    def toPositionedItem(self):
        return posmodel.PositionedItem(posmodel.GeoPosition(lat = self.position.lat,
                                                            lon = self.position.lon),
                                                            self.mid)        
