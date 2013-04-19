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
    from gaemodel import timetables
    from gaemodel import stops
    modeltt, keys, ids = testCreateTimetable()
    outString = ""
    for i in ids:
        outString += str(stops.getGAEStopByModelId(i))
    for k in keys:
        outString += str(k.get())
    gtt = timetables.getGAETimetable(modeltt)
    gttKey = gtt.put()
#     outString = None
#     if gtt != None:
#         outString = gtt.toTimetable().toXmlString()
    from gaemodel import transits
    generictransit = transits.GAETransit()
    generictransit.ttable = gttKey
    generictransit.put()
     
 
    return(outString)


class MainPage(webapp.RequestHandler):

    def get(self):
        ttable = test()
        self.response.headers['Content-Type'] = "text/plain"
        self.response.out.write("Hello!\n")
        self.response.out.write(str(ttable) + "\n")
     
Application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    
def main():
    run_wsgi_app(Application)
    
if __name__ == "__main__":
    main()
    
