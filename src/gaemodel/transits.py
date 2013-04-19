'''
Created on Apr 19, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb

import gaemodel.position as gaepos
import gaemodel.timetables as gaettable

# TODO Implement all conversion functions

class GAETransit(gaepos.GAEGeoPositionedItem):
    ttable = ndb.KeyProperty(kind=gaettable.GAETimetables, default=None)

# TODO: GAEPublicTransit Implementation
class GAEPublicTransit(GAETransit):
    pass

# TODO: GAEPrivateTransit Implementation
class GAEPrivateTransit(GAETransit):
    pass
