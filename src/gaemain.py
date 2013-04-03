'''
Created on Mar 26, 2013

@author: Michele Schimd
'''


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = "text/plain"
        self.response.out.write("Hello by Social Mobility")
    
    
Application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    
def main():
    run_wsgi_app(Application)
    
if __name__ == "__main__":
    main()
    
