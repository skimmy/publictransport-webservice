import cherrypy
import public.PublicTransits as publict

class RootService:
    
    pub = publict.PublicTransitWS();
    
    @cherrypy.expose
    def index(self):
        return "Hello from WS"
    
    @cherrypy.expose
    def default(self):
        return "Error locating service";
    

if __name__ == "__main__":    
    cherrypy.quickstart(RootService())

    