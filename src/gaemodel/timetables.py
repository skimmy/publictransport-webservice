'''
Created on Apr 8, 2013

@author: Michele Schimd
'''

from google.appengine.ext.ndb import polymodel
from google.appengine.ext import ndb

# TODO: Add conversion functions

def getGAETimetable(timetable):
    pass

class TimetableItem(ndb.Model):
    time = ndb.DateTimeProperty()
    stop = ndb.KeyProperty()

class GAETimetables(polymodel.PolyModel):
    inittime = ndb.DateTimeProperty()
    initstop = ndb.KeyProperty()
    table = ndb.StructuredProperty(TimetableItem, repeated=True)
    
    def toTimetable(self):
        pass
