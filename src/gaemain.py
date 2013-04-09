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
    import model.stops as mstops
    from model import position
    mstop = mstops.Stop(sid="stop1", pos=position.GeoPosition(lat=44.0, lon=10.9))
    mstop2 = mstops.Stop(sid="nearby", pos=position.GeoPosition(lat=44.5, lon=11.3))
    stop = gaestops.getGAEStop(mstop)
    stop2 = gaestops.getGAEStop(mstop2)
    # stop = gaestops.GAEStop(mid="stop1", position=ndb.GeoPt(0.1,8.9))
    stop.put()
    stop2.put()
    item = tt.TimetableItem(time=datetime.datetime.now(), stop=stop.key)
    item2 = tt.TimetableItem(time=(datetime.datetime.now() + datetime.timedelta(hours=1)), stop=stop2.key)
    ttable = tt.GAETimetables(initstop=None, inittime=datetime.datetime.now(), table=[item, item2])
    ttable.put()
    return ttable
        


class MainPage(webapp.RequestHandler):

    def get(self):
        ttable = test()
        self.response.headers['Content-Type'] = "text/plain"
        self.response.out.write("Hello!\n")
        for i in ttable.table:
            s = "None"
            originalstop = "None"
            if i.stop != None:
                s = i.stop.get().mid
                originalstop = i.stop.get().toStop()
            self.response.write("Stop: " + str(s) + " - " + str(i.time) + "\n\t" + str(originalstop) + "\n")
    
Application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    
def main():
    run_wsgi_app(Application)
    
if __name__ == "__main__":
    main()
    
