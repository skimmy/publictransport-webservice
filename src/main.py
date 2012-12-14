import cherrypy
import public.pubtransits as publict
import os.path

import model.users as user

class RootService:
    
    pub = publict.PublicTransitWS();
    
    def __init__(self):
        self.u = user.User("user@email.dom")
        self.u.setName("skimmy")
    
    @cherrypy.expose
    def index(self):
        return "Hello from WS"
    
    @cherrypy.expose
    def default(self):
        return "Error locating service";
    
    @cherrypy.expose
    def users(self):
        return self.u.toXmlString() 
    

if __name__ == "__main__":
    configFile = "./st.conf"
    if (os.path.isfile(configFile)):
        cherrypy.config.update(configFile)
    cherrypy.quickstart(RootService())

    