'''
Created on 31/mag/2013

@author: Michele Schimd
'''

from google.appengine.ext import endpoints
from protorpc import remote

from messages import GeoPointWithAccuracyMessage
from messages import TimedPositionMessage
from messages import ReplyInfoMessage
from messages import PositionedItemMessage
from messages import RouteMessage

import gaemodel.position as gpos
import gaemodel.route as groute

@endpoints.api(name='ptstore', version='v1', 
               description='Store API for Public Transport Web Service')
class StoreWS(remote.Service):

    @endpoints.method(GeoPointWithAccuracyMessage,
                      ReplyInfoMessage,
                      name="ptstore.store_geo_point",
                      path="storegeopt",
                      http_method='POST')
    def storeGeoPt(self, request):
        posString = "(" + str(request.longitude) + "," + str(request.latitude) + ")"
        infoString = "Ok! Position " + posString + " inserted" 
        return ReplyInfoMessage(info=infoString)
    
    @endpoints.method(PositionedItemMessage,
                      ReplyInfoMessage,
                      name="store_positioned_item", path="storepitem",
                      http_method="POST")
    def storeGeoPositionedItem(self, request):
        gaePItem = gpos.posItemMessageToGAEGeoPositionedItem(request)
        gaePItem.put()
        return ReplyInfoMessage(info="Stored")
    
    @endpoints.method(TimedPositionMessage,
                      ReplyInfoMessage,
                      name="store_timed_position", path="storetimedposition",
                      http_method='POST')
    def storeTimedPosition(self, request):
        gtimed = gpos.timedPosMessageToGAETimedPosition(request)
        gtimed.put()    
        return ReplyInfoMessage(info="Stored")
    
    @endpoints.method(RouteMessage,
                      ReplyInfoMessage,
                      name="store_route", path="storeroute",
                      http_method='POST')
    def storeRoute(self, request):
        gaeRoute = groute.routeMessageToGAERoute(request)
        gaeRoute.put()
        return ReplyInfoMessage(info="Route stored!")
    