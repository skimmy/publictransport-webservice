'''
Created on Jun 10, 2013

@author: Michele Schimd
'''

import gis.exp.parsers as mparse

# returns the list with only speeds
def getSpeedList(posList):
    speeds = []
    for p in posList:
        speeds.append(p.speed)
    return speeds

# Compute speed with accuracy
def computeSpeedsWithAccuracy(posList):
    if len(posList) < 2:
        return []
    accSpeeds = [0.0]
    prev = posList[0]
    for i in range(1,len(posList)):
        acc = float(prev.accuracy / 2.0) + float(posList[i].accuracy / 2.0)
        t = float(posList[i].secondsSince(prev))
        s = float(posList[i].distance) - acc
        accSpeed = max(3.6 * s / t,0)
        accSpeeds.append(accSpeed)
        prev = posList[i]
    return accSpeeds

# This main is just experiments
if __name__ == "__main__":
    fileName = "/home/skimmy/Desktop/NoalePD_20130530.txt"
    posList = mparse.logFileToLoggedPosList(fileName)
    x = range(len(posList))
    accSpeeds = computeSpeedsWithAccuracy(posList)
    speeds = getSpeedList(posList)    
    from pylab import *
    plot(x,accSpeeds)
    hold(True)
    plot(x,speeds,'r')
    show()
     
