'''
Created on 31/mag/2013

@author: Michele Schimd
'''

from google.appengine.ext import endpoints
from protorpc import remote

from messages import GreetingTestMessage
from messages import GeoPointWithAccuracyMessage
from messages import ReplyInfoMessage
from messages import PositionedItemMessage
from messages import KeyReplyMessage

@endpoints.api(name='ptstore', version='v1', 
               description='Store API for Public Transport Web Service')
class StoreWS(remote.Service):
    @endpoints.method(GreetingTestMessage,
                      GreetingTestMessage,
                      name="storeGreetings.greet", path='greet',
                      http_method='POST')
    def storeGreetings(self, request):
        return request

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
                      KeyReplyMessage,
                      name="store_positioned_item", path="storepitem",
                      http_method="POST")
    def storeGeoPositionedItem(self, request):
        from gaemodel.position import GAEGeoPositionedItem
        from gaemodel.position import GAEPosition
        position = GAEPosition(lat=request.position.latitude,
							   lon=request.position.longitude,
								accuracy=request.position.accuracy)
        gaePItem = GAEGeoPositionedItem(position=position,
                                        mid=request.itemId)
        storerId = gaePItem.put()
        return KeyReplyMessage(storerKey=str(storerId))
    