'''
Created on Apr 8, 2013

@author: Michele Schimd
'''

from google.appengine.ext.ndb import polymodel
from google.appengine.ext import ndb


# TODO: Add conversion functions (needs getGAEStopById() )

def getGAETimetable(timetable):
    gaetable = []
    modeltable = timetable.table
    for item in modeltable:
        gaetable.append(TimetableItem(time=item[0].seconds, stop=item[1]))
        
    return GAETimetables(initstop=timetable.initial[0],
                         inittime=timetable.initial[1],
                         table=gaetable)

class TimetableItem(ndb.Model):
    # Pay attention that this 'time' is actually a timedelta 
    # expressed in seconds as an integer
    time = ndb.IntegerProperty()
    stop = ndb.KeyProperty()

class GAETimetables(polymodel.PolyModel):
    inittime = ndb.DateTimeProperty()
    initstop = ndb.KeyProperty()
    table = ndb.StructuredProperty(TimetableItem, repeated=True)
    
    def toTimetable(self):
        pass
