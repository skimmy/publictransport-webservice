'''
Created on Mar 26, 2013

@author: Michele Schimd
'''


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def testCreateTimetable():
    from model.stops import Stop
    from gaemodel import stops
    import datetime
    from model.timetables import Timetable
    from model.position import GeoPosition
    inS = Stop("1200", GeoPosition(11.23, 47.862))
    s = Stop("1234", GeoPosition(11.12, 48.49))
    p = Stop("1235", GeoPosition(11.23, 48.33))
    t = Stop("1202", GeoPosition(11.20, 58.40))
    kinS = stops.getGAEStop(inS).put()
    ks = stops.getGAEStop(s).put()
    ps = stops.getGAEStop(p).put()
    ts = stops.getGAEStop(t).put()
    inT = datetime.time(hour=12, minute=30)
    x = datetime.timedelta(minutes=2)
    y = datetime.timedelta(minutes=5)
    z = datetime.timedelta(minutes=3)    
    tt = Timetable(inS,inT)    
    tt.insertItem(x, s)
    tt.insertItem(y, p)
    tt.insertItem(z, t)
    return tt, [kinS, ks, ps, ts], ["1200", "1234", "1235", "1202"]

def test():
    import model.position as mpos
    import gaemodel.position as gpos
    pos = mpos.GeoPosition(-30.0, 40.0)
    pos2 = mpos.GeoPosition(1.0, 40.0)    
    pos3 = mpos.GeoPosition(0.0, 41.0)
    pi = mpos.PositionedItem(pos,1234)
    return (gpos.getGAEGeoPositionedItem(pi))
 


class MainPage(webapp.RequestHandler):

    def get(self):
        ttable = test()
        ttable.put()
        self.response.headers['Content-Type'] = "text/plain"
        self.response.out.write("\n\nHello!\n")
        self.response.out.write(str(ttable) + "\n")
     
Application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    
def main():
    run_wsgi_app(Application)
    
if __name__ == "__main__":
    main()
    
