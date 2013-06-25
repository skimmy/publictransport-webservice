'''
Created on 21/giu/2013

@author: Michele Schimd
'''

from protorpc import remote

from google.appengine.ext import endpoints
from google.appengine.ext import ndb

import gaemodel.position as gaepos

from docsearch import documents
from docsearch import dochelper

from messages import PositionedItemListMessage
from messages import PositionedItemMessage
from messages import GeoPointWithAccuracyMessage
from messages import ReplyInfoMessage
import messages as msg

@endpoints.api(name='pttest', version='0.1', 
               description='Store API for Public Transport Web Service')
class TestAPI(remote.Service):
    @endpoints.method(GeoPointWithAccuracyMessage,
                      PositionedItemListMessage,
                      name='getstops', path='stops',
                      http_method='POST')
    def getStops(self, request):
        # get the documents from the text index
        docs = dochelper.getDocumentsForProximitySerch(request.latitude,
                                                       request.longitude,
                                                       request.accuracy,
                                                       dochelper.POSITIONED_ITEM_INDEX)
        gaeresult = []
        i = ""
        for d in docs:
            k = d.doc_id
            i += " " + str(k)
            dsKey = ndb.Key(urlsafe=k)
            gaeresult.append(dsKey.get())
        mesresult = []
        for r in gaeresult:
            mesresult.append(msg.gaePosItemToPosItemMessage(r))
        infoMsg = ReplyInfoMessage(info=i)
        return PositionedItemListMessage(items=mesresult, infoMessage=infoMsg)
    
    @endpoints.method(PositionedItemMessage,
                      ReplyInfoMessage,
                      name='addstop', path="stop_insert",
                      http_method='POST')
    def addStop(self, request):
        gstop = gaepos.posItemMessageToGAEGeoPositionedItem(request)
        gaeKey = gstop.put()
        doc = documents.createPositionedItemDocument(gstop, gaeKey.urlsafe())
        dochelper.storeDocumentOnIndex(doc, dochelper.POSITIONED_ITEM_INDEX)        
        # TODO: add to the full text search
        return ReplyInfoMessage(info="Ok")
    
    
            
