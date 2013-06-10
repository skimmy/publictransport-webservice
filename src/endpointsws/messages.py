'''
Created on 31/mag/2013

@author: Michele Schimd
'''

from protorpc import messages


##### DEFINITION OF USEFUL CONSTANTS #####
NO_ERROR = 0

##### DEFINITION OF MESSAGES #####

class GeoPointWithAccuracyMessage(messages.Message):
    """The base position message. Positions are define by latitude
    longitude and an optional accuracy as floats"""
    latitude = messages.FloatField(1, required=True)
    longitude = messages.FloatField(2, required=True)
    accuracy = messages.FloatField(3)
    
class PositionedItemMessage(messages.Message):
    """This is the message representing Positioned Items, positioned
    items are defined at least by an id, a position and a type.
    Other optional fields are: comments, pictures
    """
    itemId = messages.StringField(1, required=True)
    position = messages.MessageField(GeoPointWithAccuracyMessage, 2, required=True)
    # TODO: Make it required and update calling methods
    type = messages.StringField(3)
    # This may contains actual comments or id to the corresponding full text search index
    comments = messages.StringField(4, repeated=True)
    # This is a list of identifier for pictures
    pictures = messages.StringField(5, repeated=True)
    
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
    
