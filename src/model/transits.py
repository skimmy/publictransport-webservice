'''
Created on Dec 6, 2012

@author: Michele Schimd
'''

import xml.etree.ElementTree as ET

from position import GeoPosition

import timetables
import position


class Transit(position.PositionedItem):
    
    def __init__(self, tid, pos):
        position.PositionedItem.__init__(self, pos, tid)
        self.timetable = timetables.Timetable()
        
    def setTimetable(self, ttable):
        self.timetable = ttable
        
    def getTimetable(self):
        return self.timetable
    
    def toDictionary(self):
        d = position.PositionedItem.toDictionary(self)
        d['timetable'] = self.timetable
        return d
    
    def addInfoToElement(self, elem):
        position.PositionedItem.addInfoToElement(self, elem)
        ttelem = ET.SubElement(elem, 'timetable')
        self.timetable.addInfoToElement(ttelem)
        
        
    def toXmlString(self):
        e = ET.Element('transit')
        self.addInfoToElement(e)
        return ET.tostring(e)
        
class PublicTransit(Transit):
    def __init__(self, tid, pos):
        Transit.__init__(self, pos, tid)

class PrivateTransit(Transit):
    def __init__(self, tid, pos):
        Transit.__init__(self, tid, pos)

if __name__ == "__main__":    
    gp = GeoPosition(1.1, -45.78)
    tid = 1024
    tr = PrivateTransit(tid, gp)    
    print(tr.toXmlString())
