'''
Created on 07/giu/2013

@author: Michele Schimd
'''

from google.appengine.api import search

_TEST_INDEX="test"

def createPositionDocument(doc_id, gaepos):
    geoPt = search.GeoPoint(gaepos.lat, gaepos.lon)
    d = search.Document(fields=[search.TextField(name="id", value=doc_id),
                                search.GeoField(name="position", value=geoPt)])
    return d

def createPositionedItemDocument(pItem, itemStorerId):
    posField = search.GeoField(name='position',
                               value=search.GeoPoint(pItem.position.lat,
                                                     pItem.position.lon))
    d = search.Document(doc_id=itemStorerId,
                    fields=[posField])
    return d
