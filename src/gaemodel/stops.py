'''
Created on Apr 8, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb

import position as gaepos
import model.position as modelpos
from model import stops

def getGAEStopByModelId(mid):
    """Return a GAEStop with specified mid"""
    result = GAEStop.query(GAEStop.mid == mid).fetch()
    # zero length means no entity with specified mid, return None
    if len(result) <= 0:
        result = [None]
    # since twice the same id should not be allowed in 
    # such situation we can return the only available results
    return result[0]

def getGAEStop(stop):
    """Return a GaeStop created from the given Stop model class"""
    return GAEStop(mid=stop.id, position=ndb.GeoPt(stop.position.latitude,
                                                   stop.position.longitude)) 
###### GAEStop class ######

class GAEStop(gaepos.GAEGeoPositionedItem):
    def toStop(self):
        return stops.Stop(self.mid, modelpos.GeoPosition(lat=self.position.lat, lon=self.position.lon))
