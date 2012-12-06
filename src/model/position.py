'''
Created on Dec 6, 2012

@author: Michele Schimd
'''

import base

class Position(object):
    
    def getPosition(self):
        pass


class GeoPosition(Position):
    
    def __init__(self, lat=0.0, lon=0.0):
        self.latitude = lat
        self.longitude = lon
        
    def getPosition(self):
        return (self.latitude, self.longitude)
    
    def getLatitude(self):
        return self.latitude
    
    def getLongitude(self):
        return self.longitude
    
    def setPosition(self, lat, lon):
        self.latitude = lat
        self.longitude = lon
        
class PositionedItem(base.ModelBase):
    
    def __init__(self, pos, itemId):
        base.ModelBase.__init__(self, itemId)
        
        #base.ModelBase.__init__(self, itemId)
        self.position = pos
    
    def getPosition(self):        
        return self.position.getPosition()
    
    
if __name__ == "__main__":
    pos = GeoPosition(1.0,-3.0)
    item = PositionedItem(pos)
    print(item.getPosition()) 