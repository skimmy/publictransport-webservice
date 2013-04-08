'''
Created on Mar 26, 2013

@author: Michele Schimd
'''


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import ndb
import gaemodel.stops as gaestops

def test():
    import gaemodel.timetables as tt
        
    import datetime
    
    stop = gaestops.GAEStop(mid="stop1", position=ndb.GeoPt(0.1,8.9))
    stop.put()    
    item = tt.TimetableItem(time=datetime.datetime.now(), stop=stop.key)
    item2 = tt.TimetableItem(time=(datetime.datetime.now() + datetime.timedelta(hours=1)), stop=None)
    ttable = tt.GAETimetables(initstop=None, inittime=datetime.datetime.now(), table=[item, item2])
#     ttable.put()
#     return ttable
#        


class MainPage(webapp.RequestHandler):

    def get(self):
        ttable = test()
        self.response.headers['Content-Type'] = "text/plain"
        self.response.out.write("Hello!\n")
#         for i in ttable.table:
#             s = "None"
#             if i.stop != None:
#                 s = gaestops.GAEStop.
#             self.response.write("Stop: " + s + "\n")
    
Application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    
def main():
    run_wsgi_app(Application)
    
if __name__ == "__main__":
    main()
    
