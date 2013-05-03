'''
Created on Apr 4, 2013

@author: Michele Schimd
'''

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

from model import base

# def getGAEBaseModel(baseModel):
#     return GAEBaseModel(mid = baseModel.id)
# 
# class GAEBaseModel(polymodel.PolyModel):
#     mid = ndb.StringProperty()
#     
#     def toBaseModel(self):
#         return base.ModelBase(str(self.mid))
