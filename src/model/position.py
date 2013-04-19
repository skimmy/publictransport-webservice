'''
Created on Dec 6, 2012

@author: Michele Schimd
'''

import base
from gis.util import coordinates

import xml.etree.ElementTree as ET

class Position(object):
    
    accuracy = 0.0
    
    def getPosition(self):
        pass
    
    def getAccuracy(self):
        return self.accuracy
    
    def setAccuracy(self, acc):
        self.accuracy = acc


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
        
    def toDict(self):
        d = {}
        d["latitude"] = str(self.latitude)
        d["longitude"] = str(self.longitude)
        return d
    
    def toList(self):
        return [self.latitude, self.longitude]
    
    def distanceFrom(self, otherPos):
        return coordinates.distance(self.toList(), otherPos.toList())
        
class PositionedItem(base.ModelBase):
    
    def __init__(self, pos, itemId):
        base.ModelBase.__init__(self, itemId)
        self.position = pos
    
    def getPosition(self):        
        return self.position.getPosition()
    
    def setPosition(self, pos):
        self.position = pos
        
    def addInfoToElement(self, elem):
        base.ModelBase.addInfoToElement(self, elem)
        ET.SubElement(elem, "position", self.position.toDict())
        
    def toDictionary(self):
        d = base.ModelBase.toDictionary(self)
        d["position"] = self.position
        return d
        
    def toXmlString(self):
        elem = ET.Element("PositionedItem")
        self.addInfoToElement(elem)
        return ET.tostring(elem)
        
if __name__ == "__main__":
    pos = GeoPosition(0.0, 40.0)
    pos2 = GeoPosition(1.0, 40.0)    
    pos3 = GeoPosition(0.0, 41.0)
    pi = PositionedItem(pos,1234)
    print(pi.toDictionary())
    print(pi.toXmlString())
    
    print "Kilometers per lat degree   " + str(pos.distanceFrom(pos2) / 1000.0)
    print "Kilometers per lon degree   " + str(pos.distanceFrom(pos3) / 1000.0)
