'''
Created on Dec 4, 2012

@author: Michele Schimd
'''

import cherrypy
import json

class PublicTransitWS:    
    '''
    classdocs
    '''
    
    def __init__(self):
        self.properties = {}
        self.properties["code"] = "1"
        self.properties["name"] = "Transit Name"
    
    @cherrypy.expose
    def index(self):
        return "Here are the public infos"
    
    @cherrypy.expose
    def info(self):
        return json.dumps(self.properties)
    
    
        