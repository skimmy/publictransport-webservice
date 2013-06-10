'''
Created on Jun 10, 2013

@author: Michele Schimd
'''

import utility.timeutil as tutil
import datetime

class LoggedPosition:
    timestamp = None

    latitute = 0.0
    longitude = 0.0
    accuracy = 0.0   
    
    provider = ''
    
    distance = 0.0
    speed = 0.0
    bearing = 0.0
    
    def fromLogLine(self, line):
        logList = line.split()
        timeString = logList[0] + ' ' + logList[1]
        self.timestamp = tutil.stringToDatetime(timeString)[0]        
        self.latitute = float(logList[2])
        self.longitude = float(logList[3])
        self.accuracy = float(logList[4])
        self.provider = logList[5]
        self.distance = logList[6]
        self.bearing = logList[7]
        self.speed = logList[8]        
        
    def secondsSince(self, previous):
        return (self.timestamp - previous.timestamp).seconds        
        
    def __str__(self):        
        s =  "--- " + str(self.timestamp) + " ---\n"
        s += "(" + str(self.latitute) + "," + str(self.longitude) + ") - " + str(self.accuracy)
        s += "\n[" + self.provider + "]"
        return s 

if __name__ == "__main__":
    l = "2013-05-30 07:28:32.808 45.4445144 11.9857281 10.076 fused 19.567171 -144.81976 35.220905"
    l2 = "2013-05-30 07:28:34.815 45.4444505 11.9856149 8.809 fused 11.352032 -128.72649 20.433657"
    pos = LoggedPosition()
    pos.fromLogLine(l)
    pos2 = LoggedPosition()
    pos2.fromLogLine(l2)
    pos2.secondsSince(pos)