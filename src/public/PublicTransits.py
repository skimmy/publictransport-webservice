'''
Created on Dec 4, 2012

@author: Michele Schimd
'''

import cherrypy

class PublicTransit:
    '''
    classdocs
    '''
    @cherrypy.expose    
    def index(self):
        return "Here are the public infos"
    
    
        