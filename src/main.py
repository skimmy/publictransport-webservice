import cherrypy
import public.PublicTransits as publict

class RootService:
    
    pub = publict.PublicTransitWS();
    
    @cherrypy.expose
    def index(self):
        return "Hello from WS"
    
    @cherrypy.expose
    def echo(self, msg):
        return msg;
    

if __name__ == "__main__":    
    cherrypy.quickstart(RootService())

    