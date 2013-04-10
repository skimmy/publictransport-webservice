'''
Created on Apr 8, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb

import position as gaepos
import model.position as modelpos
from model import stops

# TODO: implement getGAEStopById function

def getGAEStop(stop):
    return GAEStop(mid=stop.id, position=ndb.GeoPt(stop.position.latitude,
                                                   stop.position.longitude)) 


class GAEStop(gaepos.GAEGeoPositionedItem):
    def toStop(self):
        return stops.Stop(self.mid, modelpos.GeoPosition(lat=self.position.lat, lon=self.position.lon))
