'''
Created on Dec 6, 2012

@author: Michele Schimd
'''

import xml.etree.ElementTree as ET

from position import GeoPosition


import timetables
import position


class Transit(position.PositionedItem):
    '''
        The Transit class is a direct subclass of PositionedItem, it describes transits    
    '''    
    # constructor
    def __init__(self, tid, pos, timet=None):
        position.PositionedItem.__init__(self, pos, tid)
        self.timetable = timet
        
    # get and set methods
    def setTimetable(self, ttable):
        self.timetable = ttable
        
    def getTimetable(self):
        return self.timetable
    
    # conversion methods
    def toDictionary(self):
        d = position.PositionedItem.toDictionary(self)
        d['timetable'] = self.timetable
        return d
    
    def addInfoToElement(self, elem):
        position.PositionedItem.addInfoToElement(self, elem)
        ttelem = ET.SubElement(elem, 'timetable')
        if(self.timetable != None):
            self.timetable.addInfoToElement(ttelem)        
        
    def toXmlString(self):
        e = ET.Element('transit')
        self.addInfoToElement(e)
        return ET.tostring(e)
    

        
class PublicTransit(Transit):
    def __init__(self, tid, pos, tt=None):
        Transit.__init__(self, pos, tid, tt)


class PrivateTransit(Transit):
    '''
        PrivateTransit is a transit with an associated owner, such owenr must be a registred 
        user of the serivice (i.e. owner is of type User).        
    '''
    
    # constructor
    def __init__(self, tid, pos, tt=None):
        Transit.__init__(self, tid, pos, tt)
        self.owner = None
    
    # get and set methods
    def setOwner(self, ow):
        self.owner = ow
        
    def getOwner(self):
        return self.owner
    
    # conversion methods   
    def addInfoToElement(self, elem):
        Transit.addInfoToElement(self, elem)
        uid = ""
        if (self.owner != None):
            uid = self.owner.getId() 
        ET.SubElement(elem, "owner", oid=uid)
        
    def toXmlString(self):
        e = ET.Element("PrivateTransit")
        self.addInfoToElement(e)
        return ET.tostring(e)

if __name__ == "__main__":
    import datetime
    import stops
    import users
    gp = GeoPosition(1.1, -45.78)
    tid = 1024
    tt = timetables.Timetable(stops.Stop("10",gp),datetime.time(hour=9, minute=45))
    tr = PrivateTransit(tid, gp, tt)
    tr.setOwner(users.User("me@ex.mp"))
    print(tr.toXmlString())
