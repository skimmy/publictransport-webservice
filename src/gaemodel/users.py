'''
Created on Apr 8, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb

import position

# TODO: Add conversion functions (need timetable GAE class)

###### USERSESSION CLASS ######

class GAEUserSession(ndb.Model):
    starttime = ndb.DateTimeProperty()
    timetable = ndb.KeyProperty()
    
    
##### USER CLASS #####

class GAEUser(position.GAEGeoPositionedItem):
    name = ndb.StringProperty()
