'''
Created on 31/mag/2013

@author: Michele Schimd
'''

from protorpc import messages


##### DEFINITION OF USEFUL CONSTANTS #####
NO_ERROR = 0

##### DEFINITION OF MESSAGES #####

class GeoPointWithAccuracyMessage(messages.Message):
    latitude = messages.FloatField(1, required=True)
    longitude = messages.FloatField(2, required=True)
    accuracy = messages.FloatField(3)
    
class PositionedItemMessage(messages.Message):
    itemId = messages.StringField(1, required=True)
    position = messages.MessageField(GeoPointWithAccuracyMessage, 2, required=True)
    
class TimedPositionMessage(messages.Message):
    position = messages.MessageField(GeoPointWithAccuracyMessage, 1, required=True)
    timestamp = messages.StringField(2, required=True)
    
class RouteMessage(messages.Message):
    positions = messages.MessageField(TimedPositionMessage, 1, 
                                      repeated=True)
class NeighbourSearchMessage(messages.Message):
    position = messages.MessageField(GeoPointWithAccuracyMessage, 1,
                                     required=True)
    radius = messages.FloatField(2,required=True) 
    
class ReplyInfoMessage(messages.Message):
    info = messages.StringField(1, required=True)
    errorCode = messages.IntegerField(2)
    
