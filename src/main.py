import cherrypy
import public.PublicTransits as publict

class RootService:
    
    pub = publict.PublicTransit();
    
    def index(self):
        return "Hello from WS"
    index.exposed = True


if __name__ == "__main__":    
    cherrypy.quickstart(RootService())

    