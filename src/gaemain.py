'''
Created on Mar 26, 2013

@author: Michele Schimd
'''


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def test():
    import model.position as pos
    import gaemodel.position as gaepos
    p1 = pos.PositionedItem(pos.GeoPosition(1.234, 45.999), "sk")
    gp1 = gaepos.getGAEGeoPositionedItem(p1)
    return [gp1.toPositionedItem()]
    


class MainPage(webapp.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = "text/plain"
        for p in test():
            self.response.out.write(p.toXmlString())
    
Application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    
def main():
    run_wsgi_app(Application)
    
if __name__ == "__main__":
    main()
    
