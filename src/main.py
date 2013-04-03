import cherrypy
import public.pubtransits as publict

from google.appengine.ext.webapp.util import run_wsgi_app

import model.users as user

class RootService:
    
    pub = publict.PublicTransitWS();
    
    
    def __init__(self):
        self.u = user.User("user@email.dom")
        self.u.setName("skimmy")
    
    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return "Hello from WS"
    
    @cherrypy.expose
    def default(self):
        
        return "Error locating service";
    
    @cherrypy.expose
    def users(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return self.u.toXmlString() 
    

if __name__ == "__main__":    
    app = cherrypy.tree.mount(RootService(), '/')
     
    run_wsgi_app(app)

    