'''
Created on Dec 6, 2012

@author: Michele Schimd
'''

import base

class Position(object):
    
    def getPosition(self):
        pass


class GeoPosition(Position):
    '''
        This is a position represented in geographical form that is, position
        is represented as latitude and longitude.            
    '''
    
    DIGIT_PRECISION = 6 
    
    def __init__(self, lat=0.0, lon=0.0):
        '''
            The constructor initializes the position by giving its latitude and
            longitude. If no parameter is given, then the position is set to the
            default value (0,0)
        '''
        self.latitude = lat
        self.longitude = lon
        
    def __repr__(self):
        return ("(" + str(round(self.latitude, self.DIGIT_PRECISION)) + ", " + str(round(self.longitude, self.DIGIT_PRECISION)) + ")")
        
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
        self.position = pos
    
    def getPosition(self):        
        return self.position.getPosition()
    
    def setPosition(self, pos):
        self.position = pos
    
    
if __name__ == "__main__":
    pos = GeoPosition(1.0, -3.0)
    item = PositionedItem(pos)
    print(item.getPosition()) 
