'''
Created on 31/mag/2013

@author: Michele Schimd
'''

from google.appengine.ext import endpoints
from protorpc import remote

import messages as msgs
from messages import GeoPointWithAccuracyMessage
from messages import TimedPositionMessage
from messages import ReplyInfoMessage
from messages import PositionedItemMessage
from messages import RouteMessage

import gaemodel.position as gpos
import gaemodel.route as groute

from docsearch import documents
from docsearch import dochelper

@endpoints.api(name='ptstore', version='v0.1', 
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
        """This is the method to store a new positioned item. Since
        positioned item are supposed to be searched by location
        vicinity, they should also be stored on the 'Full Text Search'
        index in order to allow location based searches.
        """
        # create GAE model object from message and put in the storer
        gaePItem = gpos.posItemMessageToGAEGeoPositionedItem(request)
        storerKey = gaePItem.put()
        # with the Key of the data storer create the document ID
        doc = documents.createPositionedItemDocument(gaePItem, storerKey.urlsafe())
        # TODO: Define indices for various type of positioned items or just use a single big index??
        # store the document in  the proper index
        dochelper.storeDocumentOnIndex(doc, dochelper.POSITIONED_ITEM_INDEX)
        return ReplyInfoMessage(info="Ok", errorCode=msgs.NO_ERROR)
    
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
    