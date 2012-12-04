import cherrypy
import public.PublicTransits as publict
import os.path

class RootService:
    
    pub = publict.PublicTransitWS();
    
    @cherrypy.expose
    def index(self):
        return "Hello from WS"
    
    @cherrypy.expose
    def default(self):
        return "Error locating service";
    

if __name__ == "__main__":
    configFile = "./st.conf"
    if (os.path.isfile(configFile)):
        cherrypy.config.update(configFile)
    cherrypy.quickstart(RootService())

    