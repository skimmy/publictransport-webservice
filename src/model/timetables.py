'''
Created on Dec 6, 2012

@author: Michele Schimd
'''

import datetime

from stops import Stop
from position import GeoPosition

class Timetable:
    '''
        The Timetable class is an aggregation class for deltatime / stop pairs
        with initial stop and time. Each element (different from the initial) is
        a stop object with elapsed time from the starting point
    '''
    
    def __init__(self, initStop, initTime):
        self.initial = (initTime, initStop)
        self.table = []
        
    def setInitial(self, initialTime, initialPosition):
        self.initial = (initialTime, initialPosition)
        
    def insertItem(self, t, s):
        self.table.append( (t,s) )
    
    def getSortedTimetable(self):
        toReturn = [self.initial]
        toReturn.extend(sorted(self.table,key=lambda item : item[0]))
        return toReturn

if __name__ == "__main__":
    inS = Stop("1200", GeoPosition(11.23, 47.862))
    s = Stop("1234", GeoPosition(11.12, 48.49))
    p = Stop("1235", GeoPosition(11.23, 48.33))
    t = Stop("1200", GeoPosition(11.20, 58.40))
    
    inT = datetime.time(hour=12, minute=30)
    x = datetime.timedelta(minutes=2)
    y = datetime.timedelta(minutes=5)
    z = datetime.timedelta(minutes=3)
    
    tt = Timetable(inS,inT)
    
    tt.insertItem(x, s)
    tt.insertItem(y, p)
    tt.insertItem(z, t)
    

    sortedTt = tt.getSortedTimetable()
    for tti in sortedTt:
        print(tti)
        
    
    
    