'''
Created on Apr 4, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import model.position as posmodel
# import endpointsws.messages as messages

###### CONVERSION FUNCTIONS #####

def getGAEGeoPositionedItem(item):
    pos = GAEPosition(lat = item.position.latitude,
                      lon = item.position.longitude,
                      accuracy = item.position.accuracy)
    return GAEGeoPositionedItem(position=pos,
                                mid=item.id)
    
def posItemMessageToGAEGeoPositionedItem(msg):
    pos = geoPointMessageToGAEPosition(msg.position)
    itemId = msg.itemId
    return GAEGeoPositionedItem(position=pos, mid=itemId)
    
def geoPointMessageToGAEPosition(msg):
    return GAEPosition(lat=msg.latitude,
                       lon=msg.longitude,
                       accuracy=msg.accuracy)
    
def timedPosMessageToGAETimedPosition(msg):
    import utility.timeutil as timeutil
    pos = geoPointMessageToGAEPosition(msg.position)
    tstamp= timeutil.stringToDatetime(msg.timestamp)[0]
    return GAETimedPosition(position=pos,
                            timestamp=tstamp)

    
###### GAE POSITION CLASS #####
   
class GAEPosition(ndb.Model):
    lat = ndb.FloatProperty()
    lon = ndb.FloatProperty()
    accuracy = ndb.FloatProperty()


###### GAE POSITIONED ITEM CLASS #####

class GAEGeoPositionedItem(polymodel.PolyModel):    
    mid = ndb.StringProperty()
    position = ndb.StructuredProperty(GAEPosition)

    def toPositionedItem(self):
        p = posmodel.PositionedItem(posmodel.GeoPosition(lat = self.position.lat,
                                                         lon = self.position.lon,
                                                         acc = self.position.accuracy),
                                                         self.mid)
        p.setAccuracy(self.accuracy)
        return p
    
##### GAE TIMED ITEM CLASS #####
class GAETimedPosition(ndb.Model):
    position = ndb.StructuredProperty(GAEPosition)
    timestamp = ndb.DateTimeProperty()   

