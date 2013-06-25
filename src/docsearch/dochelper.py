'''
Created on 09/giu/2013

@author: Michele Schimd
'''

from google.appengine.api import search
from google.appengine.ext.ndb import Key

#### CONSTANTS DEFINITIONS #####

POSITIONED_ITEM_INDEX="positioned_item"

POSITION_FIELD_NAME="position"
DATASTOREKEY_FIELD_NAME = "id"

#### UTILITY FUNCTIONS #####

def storerKeyToDocumentId(storerKey):
    return (storerKey.kind() + '-' + str(storerKey.id()))

def documentIdToStorerKey(docId):
    splitKey = docId.split('-')
    return Key(splitKey[0], long(splitKey[1]))

##### INTERACTION WITH THE SEARCH API #####

def storeDocumentOnIndex(doc, idx):
    search.Index(name=idx).put(doc)

def execQueryStringOnIndex(query, idxName):
    index = search.Index(idxName)
    return index.search(query)

##### "STANDARD" QUERIES #####

def getDocumentsForProximitySerch(lat, lon, distance, indexName):
    fieldName = POSITION_FIELD_NAME
    query = "distance(%s, geopoint(%f,%f)) < %d" % (fieldName, lat, lon, distance)
    return execQueryStringOnIndex(query, indexName)
