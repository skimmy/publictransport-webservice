'''
Created on 31/mag/2013

@author: Michele Schimd
'''

from protorpc import messages

class GreetingTestMessage(messages.Message):
    greet = messages.StringField(1, required=True)
    
class GeoPointWithAccuracyMessage(messages.Message):
    latitude = messages.FloatField(1, required=True)
    longitude = messages.FloatField(2, required=True)
    accuracy = messages.FloatField(3)
    
class PositionedItemMessage(messages.Message):
    itemId = messages.StringField(1, required=True)
    position = messages.MessageField(GeoPointWithAccuracyMessage, 2, required=True)
    
    
class RouteMessage(messages.Message):
    positions = messages.MessageField(GeoPointWithAccuracyMessage, 1, 
                                      repeated=True)
    
class KeyReplyMessage(messages.Message):
    storerKey = messages.StringField(1, required=True)

class ReplyInfoMessage(messages.Message):
    info = messages.StringField(1, required=True)
    
    
if __name__ == "__main__":
    k = KeyReplyMessage(storerKey="aaa")
    