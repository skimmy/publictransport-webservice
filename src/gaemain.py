'''
Created on Mar 26, 2013

@author: Michele Schimd
'''


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def test():
    from model import base
    import gaemodel.base as gaebase
    b1 = base.ModelBase()
    b2 = base.ModelBase("pippo")
    gb1 = gaebase.GAEBaseModel(id = b1.id)
    gb2 = gaebase.getGAEBaseModel(b2)
    #gb2 = gaebase.GAEBaseModel(b2.toDictionary())
    return [gb1.toBaseModel(), gb2.toBaseModel()]


class MainPage(webapp.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = "text/plain"
        self.response.out.write('<root>')        
        for b in test():
            self.response.out.write(b.toXmlString())
        self.response.out.write('</root>')
     
    
Application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    
def main():
    run_wsgi_app(Application)
    
if __name__ == "__main__":
    main()
    
