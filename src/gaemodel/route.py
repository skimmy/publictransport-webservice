'''
Created on 05/giu/2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb

import gaemodel.position as gpos

##### Conversion functions #####

def routeMessageToGAERoute(msg):
    posMsgs = msg.positions;
    ps =[]
    for p in posMsgs:
        ps.append(gpos.timedPosMessageToGAETimedPosition(p))
    return GAERoute(positions=ps)
        

##### GAERoute CLASS #####

class GAERoute(ndb.Model):
    positions = ndb.StructuredProperty(gpos.GAETimedPosition, repeated=True)
