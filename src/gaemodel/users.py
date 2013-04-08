'''
Created on Apr 8, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

import position

# TODO: Add conversion functions (need timetable GAE class)

###### USERSESSION CLASS ######

class UserSession(polymodel.PolyModel):
    starttime = ndb.DateTimeProperty()
    timetable = ndb.KeyProperty()
    
    
##### USER CLASS #####

class User(position.GAEGeoPositionedItem):
    name = ndb.StringProperty()
