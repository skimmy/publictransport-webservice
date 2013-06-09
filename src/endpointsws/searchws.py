'''
Created on 08/giu/2013

@author: Michele Schimd
'''

from google.appengine.ext import endpoints
from google.appengine.api import search

from docsearch import documents
from docsearch import query
from gaemodel import position

from endpointsws.messages import NeighbourSearchMessage
from endpointsws.messages import ReplyInfoMessage

@endpoints.api(name='ptsearch', version='v0.1', 
               description='Search API for Public Transport Web Service')
class SearchWS:
    @endpoints.method(NeighbourSearchMessage,
                      ReplyInfoMessage,
                      name='neighbour_search', path='neighboursearch',
                      http_method='POS')
    def neighbourSearch(self, request):
        # get the document for the Search API
        query = query.getNeghborhoodStringQuery(request.position.latitude,
                                                request.position.longitude,
                                                request.radius, 'position')
        index = search.Index(documents.POSITIONED_ITEM_INDEX)
        results = index.search("pippo")
#         results = index.search(query)
        
        s = ""
        for r in results:
            s += str(r)
#         pos = position.geoPointMessageToGAEPosition(request.position)
#         itemId= "DefaultId"
#         gaePosItem = position.GAEGeoPositionedItem(position=pos,
#                                                    mid=itemId)
#         documents.createPositionedItemDocument(gaePosItem, itemStorerId)
                                                   