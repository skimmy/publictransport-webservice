'''
Created on Apr 8, 2013

@author: Michele Schimd
'''

import datetime

from google.appengine.ext import ndb

from gaemodel import stops
import model.timetables as mtt


# TODO (Performance): on conversion function us bulk of stops retrieves from the datastore 

def getGAETimetable(timetable):
    gaetable = []
    modeltable = timetable.table
    for item in modeltable:
        gaestop = stops.getGAEStopByModelId(item[1].id)
        if gaestop != None:
            gaetable.append(TimetableItem(time=item[0].seconds, stop=gaestop.key))
        else:
            # TODO: decide what to do when there is no proper gaestop object in the datastore
            return None
        
    initialStopEntity = stops.getGAEStopByModelId(timetable.initial[1].id)
    if initialStopEntity != None:
        initialStopKey = initialStopEntity.key
    else:
        return None
    return GAETimetables(initstop=initialStopKey,
                         inittime=timetable.initial[0],
                         table=gaetable)

class TimetableItem(ndb.Model):
    # Pay attention that this 'time' is actually a timedelta 
    # expressed in seconds as an integer
    time = ndb.IntegerProperty()
    stop = ndb.KeyProperty()

class GAETimetables(ndb.Model):
    inittime = ndb.TimeProperty()
    initstop = ndb.KeyProperty()
    table = ndb.StructuredProperty(TimetableItem, repeated=True)
    
    def toTimetable(self):
        initstop = self.initstop.get().toStop()
        tt = mtt.Timetable(initStop=initstop, initTime=self.inittime)
        for item in self.table:
            s = item.stop.get().toStop()
            t = datetime.timedelta(seconds=item.time) 
            tt.insertItem(t, s)
        return tt
